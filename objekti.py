f = open("objekti.csv", "w")
for i in range(1,1003,7):
        print(i)
        f.write(str(i)+",HDD,memory,"+str(i)+"\n")
        f.write(str(i+1)+",SSD,memory,"+str(i)+"\n")
        f.write(str(i+2)+",MOBO,board,"+str(i)+"\n")
        f.write(str(i+3)+",CPU,processor,"+str(i)+"\n")
        f.write(str(i+4)+",GPU,processor,"+str(i)+"\n")
        f.write(str(i+5)+",RAM,memory,"+str(i)+"\n")
        f.write(str(i+6)+",PSU,power,"+str(i)+"\n")

f.close()

#open and read the file after the overwriting:
f = open("objekti.csv", "r")
print(f.read()) 




                               [ Read 16 lines ]
^G Help      ^O Write Out ^W Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line
