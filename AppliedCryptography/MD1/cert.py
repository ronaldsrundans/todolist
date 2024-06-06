#Ronalds Rundāns rr11043
#Solution for homework 2 (only) Step 1 

from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509

from cryptography.x509.oid import NameOID

from cryptography.hazmat.primitives import hashes
from datetime import datetime, date, time, timezone, timedelta

#arr=["US","California","San Francisco","My Company","mysite.com"]

f = open("issuer.txt", "r")
txt=(f.read()) 
arr=(txt.split('\n'))
#print(arr)
key = rsa.generate_private_key(

    public_exponent=65537,

    key_size=2048,

)

# Write our key to disk for safe keeping

with open("key.pem", "wb") as f:

    f.write(key.private_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PrivateFormat.TraditionalOpenSSL,

        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),

    ))
#CERT
# Various details about who we are. For a self-signed certificate the

# subject and issuer are always the same.

subject = issuer = x509.Name([

    x509.NameAttribute(NameOID.COUNTRY_NAME, arr[0]),

    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, arr[1]),

    x509.NameAttribute(NameOID.LOCALITY_NAME, arr[2]),

    x509.NameAttribute(NameOID.ORGANIZATION_NAME, arr[3]),

    x509.NameAttribute(NameOID.COMMON_NAME, arr[4]),

])

cert = x509.CertificateBuilder().subject_name(

    subject

).issuer_name(

    issuer

).public_key(

    key.public_key()

).serial_number(

    x509.random_serial_number()

).not_valid_before(

    #datetime.now(datetime.timezone.utc)
    datetime.now(timezone.utc)   

).not_valid_after(

    # Our certificate will be valid for 10 days

    datetime.now(timezone.utc)+ timedelta(days=10)

).add_extension(

    x509.SubjectAlternativeName([x509.DNSName("localhost")]),

    critical=False,

# Sign our certificate with our private key

).sign(key, hashes.SHA3_256() )  

# Write our certificate out to disk.

with open("cert.pem", "wb") as f:

    f.write(cert.public_bytes(serialization.Encoding.PEM))
    
#with open("key2.pem", "wb") as f:


