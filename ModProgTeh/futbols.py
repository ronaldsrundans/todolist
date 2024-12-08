
import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('team.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS TEAM")
 
# Creating table
table = """ CREATE TABLE TEAM (
            Name VARCHAR(255) NOT NULL,
            PUN_TOT INT,      
            USKPM INT,       
            ZSKPM INT,     
            UZSKPL INT,      
            ZSKPL INT,       
            IEGV INT,       
            ZAUV INT
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()


import xml.etree.ElementTree as ET

class Team:
  def __init__(self, name):
    self.name = name
    self.PUN_TOT=0      
    self.USKPM=0      
    self.ZSKPM=0     
    self.UZSKPL=0      
    self.ZSKPL=0       
    self.IEGV=0       
    self.ZAUV=0
    self.vpm=0
    self.vpl=0


for i in range (3):
  #print(i)
  tree = ET.parse('futbols'+str(i)+'.xml')
  root = tree.getroot()
  print(root.tag)
  print(root.attrib)
  komarr=[]
  vgarr=[]
  tmp=[]
  nrpk=0
  print("Neighbor2:")
  for komanda in root.iter('Komanda'):
    print(komanda.attrib)
    print("Komandas nosaukums ir "+komanda.get("Nosaukums"))
    vgarr.append(komanda.get("Nosaukums"))
    komarr.append(komanda.get("Nosaukums"))
    tmp.append(Team(komanda.get("Nosaukums")))
    nrpk+=1


    for speletaji in komanda.iter('Speletaji'):
         for speletajs in speletaji.iter('Speletajs'):
            #print(ighbor.attrib)
            rank = speletajs.get ("Uzvards")
            name = speletajs.get("Vards")
            #print(name, rank)
    print("_ Komandas sodi: ")
    for sodi in komanda.iter('Sodi'):
        for sods in sodi.iter('Sods'):
            print(sods.attrib)
    print("_ Komandas varti: ")
    for varti in komanda.iter('Varti'):
        for vg in varti.iter('VG'):
            print(vg.attrib)
            vgarr.append(vg.get("Laiks"))

            #print vg.get("Laiks")
            a = vg.get("Laiks").split(":")#"Hello, World!"
            print(a) # returns ['Hello', ' World!'] 
            if(int(a[0])>59 and int(a[1])>1):
              print("Papildlaiks!")
              #tmp[nrpk-1].UZSKPL+=1
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpl+=1
            else:
              print("Pamatlaiks!")
              #tmp[nrpk-1].USKPM+=1
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpm+=1
            #vgarr.append(vg.get("Laiks"))
    print("Statistics:")
    if (len(tmp)>1):
      print("Ieliek zaudētie vārti:")
      tmp[0].ZAUV+=(tmp[1].vpl+tmp[1].vpm )
      tmp[1].ZAUV+=(tmp[0].vpl+tmp[0].vpm )
      print("Ieliek punkti:")
      if(tmp[0].vpl>0 or tmp[1].vpl>0):
        print("Papildlaika uzvareja:")
        if(tmp[0].vpl>tmp[1].vpl):
          tmp[0].PUN_TOT+=3
          tmp[1].PUN_TOT+=2
          tmp[0].UZSKPL+=1
          tmp[1].ZSKPL+=1
        else:
          tmp[0].PUN_TOT+=2
          tmp[1].PUN_TOT+=3
          tmp[1].UZSKPL+=1
          tmp[0].ZSKPL+=1
      else:
        print("Pamatlaika uzvareja:")
        if(tmp[0].vpm>tmp[1].vpm):
          tmp[0].PUN_TOT+=5
          tmp[1].PUN_TOT+=1
          tmp[0].USKPM+=1
          tmp[1].ZSKPM+=1
        else:
          tmp[0].PUN_TOT+=1
          tmp[1].PUN_TOT+=5
          tmp[1].USKPM+=1
          tmp[0].ZSKPM+=1
              


    print("Statistics:")
    # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[0].name+"', '"+str(tmp[0].PUN_TOT)+"', '"+str(tmp[0].USKPM)+"','"+str(tmp[0].ZSKPM)+"','"+str(tmp[0].UZSKPL)+"','"+str(tmp[0].ZSKPL)+"','"+str(tmp[0].IEGV)+"','"+str(tmp[0].ZAUV)+"')") 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[1].name+"', '"+str(tmp[1].PUN_TOT)+"', '"+str(tmp[1].USKPM)+"','"+str(tmp[1].ZSKPM)+"','"+str(tmp[1].UZSKPL)+"','"+str(tmp[1].ZSKPL)+"','"+str(tmp[1].IEGV)+"','"+str(tmp[1].ZAUV)+"')") 
  conn.commit() 
  conn.close()


    #print("Statistics:")

  for x in vgarr:
    print(x)
print("TMP:  ")
for y in tmp:
  print(y.name)
  print("Iegutie vārti:")
  print(y.IEGV)
  print("Zaudētie vārti:")
  print(y.ZAUV)

# Connecting to sqlite 
conn = sqlite3.connect('team.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
data1=cursor.execute("SELECT * FROM TEAM WHERE NAME = '"+tmp[0].name+"'")
print(cursor.fetchall())

data2=cursor.execute("SELECT * FROM TEAM WHERE NAME = '"+tmp[1].name+"'")
print(cursor.fetchall())
data2=cursor.execute("SELECT * FROM TEAM WHERE NAME = 'Barcelona' ")
print(cursor.fetchall())
data3=cursor.execute("SELECT name,sum(PUN_TOT), sum(USKPM), sum(ZSKPM), sum(UZSKPL), sum(ZSKPL), sum(IEGV), sum(ZAUV) FROM TEAM group by name order by sum(PUN_TOT)")
print(cursor.fetchall())
# Queries to INSERT records. 
#cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[0].name+"', '"+str(tmp[0].PUN_TOT)+"', '"+str(tmp[0].USKPM)+"','"+str(tmp[0].ZSKPM)+"','"+str(tmp[0].UZSKPL)+"','"+str(tmp[0].ZSKPL)+"','"+str(tmp[0].IEGV)+"','"+str(tmp[0].ZAUV)+"')") 
#cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[1].name+"', '"+str(tmp[1].PUN_TOT)+"', '"+str(tmp[1].USKPM)+"','"+str(tmp[1].ZSKPM)+"','"+str(tmp[1].UZSKPL)+"','"+str(tmp[1].ZSKPL)+"','"+str(tmp[1].IEGV)+"','"+str(tmp[1].ZAUV)+"')") 
# 'UPDATE TEAM SET  = ,  = WHERE NAME="+tmp[0].name+" '
"""
data1=cursor.execute("SELECT * FROM TEAM WHERE NAME = '"+tmp[0].name+"'")

print(cursor.fetchall())
data2=cursor.execute("SELECT * FROM TEAM WHERE NAME = '"+tmp[1].name+"'")
for row in data2:
  print("ROW="+str(row[6]))
print(cursor.fetchall())


  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM TEAM''') 
for row in data: 
    print(row) 
"""  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()



#komandas nosaukums
#pamatlaikā (punktu skait, uzvaras, zaudējumi)
#papildlaikā (punktu skait, uzvaras, zaudējumi)
#
"""  for x in komarr:
    print(x)
  
for y in tmp:
  print(y.name)
  print(y.win)
  print(y.lose)


Par uzvaru pamatlaikā komanda saņem PIECUS punktus, par uzvaru papildlaikā 
komanda saņem TRĪS punktus, par zaudējumu papildlaikā komanda saņem DIVUS punktus, 
par zaudējumu pamatlaikā komanda saņem VIENU punktu. 
print("NEXT")
for country in root.findall('Speletaji'):

    #rank = country.find('rank').text
    rank = country.get ("Loma")
    name = country.get('Name')
"""
#komandas nosaukums
#pamatlaikā (punktu skait, uzvaras, zaudējumi)
#papildlaikā (punktu skait, uzvaras, zaudējumi)
#

"""turnīra tabulu (komandas vieta tabulā pēc kārtas, nosaukums, 
    iegūto punktu skaits, uzvaru un zaudējumu skaits pamatlaikā, 
    uzvaru un zaudējumu skaits papildlaikā, spēlēs gūto un zaudēto vārtu skaits). 
    Augstākā vietā jāatrodas komandai, kurai ir vairāk punktu.
    turnīra desmit rezultatīvāko spēlētāju (sakārtoti pēc gūto vārtu skaita un 
    rezultatīvo piespēļu skaita dilstošā secībā) saraksts. 
    Jānorāda vieta sarakstā pēc kārtas, spēlētāja vārds un uzvārds, 
    komandas nosaukums, gūto vārtu skaits un rezultatīvo piespēļu skaits. 
    Sarakstā augstāk jāatrodas spēlētājam, kas guvis vairāk vārtu, bet, 
    vienāda gūto vārtu skaita gadījumā, tam spēlētājam, kas vairāk reižu rezultatīvi piespēlējis."""

    #cars.append("Honda") 
"""
for child in root:

    print(child.tag, child.attrib)
print("Neighbor:")
for neighbor in root.iter('Komanda'):

    print(neighbor.attrib)
    for eighbor in neighbor.iter('Speletajs'):
         print(eighbor.attrib)
"""
#rint("Print"+root[0][1][0].text)
