
import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('team.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS TEAM")
cursor_obj.execute("DROP TABLE IF EXISTS PLAYER")

# Creating table
table = """ CREATE TABLE TEAM (
            Name VARCHAR(255) NOT NULL,
            PUN_TOT INT,      
            USKPM INT,       
            ZSKPM INT,     
            UZSKPL INT,      
            ZSKPL INT,       
            IEGV INT,       
            ZAUV INT,
            RINKIS VARCHAR(255)
        ); """
#RINKIS Name VARCHAR(255)
"""turnīra desmit rezultatīvāko spēlētāju (sakārtoti pēc gūto vārtu skaita un 
rezultatīvo piespēļu skaita dilstošā secībā) saraksts. Jānorāda vieta sarakstā pēc kārtas, 
spēlētāja vārds un uzvārds, komandas nosaukums, gūto vārtu skaits un rezultatīvo piespēļu skaits. 
Sarakstā augstāk jāatrodas spēlētājam, kas guvis vairāk vārtu, bet, vienāda gūto vārtu 
skaita gadījumā, tam spēlētājam, kas vairāk reižu rezultatīvi piespēlējis."""
cursor_obj.execute(table)
table2 = """ CREATE TABLE PLAYER (
            NR INT,            
            KOM_NOS VARCHAR(255) NOT NULL,
            VARDS VARCHAR(255) NOT NULL,
            UZVARDS VARCHAR(255) NOT NULL,
            VARTI INT,
            PIESP INT
         ); """  
         #
          #  
          #  ,
          
         #VARTI INT,
          #  PIESP INT
cursor_obj.execute(table2)

#print("Table is Ready")
 
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
#END of class Team
class Player:
  def __init__(self, Nr, Vards, Uzvards, Kom_Nos):
    self.Nr = Nr
    self.Vards = Vards
    self.Uzvards = Uzvards
    self.Kom_Nos = Kom_Nos
    self.GVSK=0
    self.RPSK=0

    #     GVSK       RPSK
#END of class Player
def my_function(i, path2,rinkis):
  tree = ET.parse(path2+'futbols'+str(i)+'.xml')
  root = tree.getroot()
  #print(root.tag)
  #print(root.attrib)
  tmp=[]
  nrpk=0
  person=[]
  #print("Neighbor2:")
  for komanda in root.iter('Komanda'):
    tmp.append(Team(komanda.get("Nosaukums")))
    nrpk+=1
    for speletaji in komanda.iter('Speletaji'):
         for speletajs in speletaji.iter('Speletajs'):
            #print(ighbor.attrib)
            surname = speletajs.get ("Uzvards")
            personname = speletajs.get("Vards")
            playernr=speletajs.get("Nr")
            playerteam=tmp[nrpk-1].name
            person.append(Player(playernr, personname, surname, playerteam))
            # Connecting to sqlite 
            conn = sqlite3.connect('team.db') 
            cursor = conn.cursor() 
            #for p in person:
            #print(p.Nr+" "+p.Vards+" "+p.Uzvards+" "+p.Kom_Nos)
            cursor.execute("INSERT INTO PLAYER VALUES ("+playernr+",'"+playerteam+"','"+personname+"','"+surname+"',0,0)")

            #cursor.execute("INSERT INTO PLAYER VALUES ("+p.Nr+",'"+p.Kom_Nos+"','"+p.Vards+"','"+p.Uzvards+"',0,0)")
            #,'"+p.Kom_Nos+"','"+p.Vards+"','"+p.Uzvards+"')") 
            conn.commit() 
            conn.close()

            #print(name, rank)
    #print("_ Komandas sodi: ")
    """
    for sodi in komanda.iter('Sodi'):
        for sods in sodi.iter('Sods'):
            print(sods.attrib)
    """
    #print("_ Komandas varti: ")
    for varti in komanda.iter('Varti'):
        for vg in varti.iter('VG'):
            a = vg.get("Laiks").split(":")#"Hello, World!"
            if(int(a[0])>59 and int(a[1])>1):
              #print("Papildlaiks!")
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpl+=1
            else:
              #print("Pamatlaiks!")
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpm+=1
            print("Vārtus iesita NR.="+vg.get("Nr"))
            #for p in vg.iter('P'):
            #  print(p.get("Nr"))
    if (len(tmp)>1):
      #print("Ieliek zaudētie vārti:")
      #speletaji
      """
      # Connecting to sqlite 
      conn = sqlite3.connect('team.db') 
      cursor = conn.cursor() 
      for p in person:
        print(p.Nr+" "+p.Vards+" "+p.Uzvards+" "+p.Kom_Nos)
        cursor.execute("INSERT INTO PLAYER VALUES ("+p.Nr+",'"+p.Kom_Nos+"','"+p.Vards+"','"+p.Uzvards+"',0,0)")
        #,'"+p.Kom_Nos+"','"+p.Vards+"','"+p.Uzvards+"')") 
      conn.commit() 
      conn.close()
      """
      # end of speletaji#
      tmp[0].ZAUV+=(tmp[1].vpl+tmp[1].vpm )
      tmp[1].ZAUV+=(tmp[0].vpl+tmp[0].vpm )
      #print("Ieliek punkti:")
      if(tmp[0].vpl>0 or tmp[1].vpl>0):
        #print("Papildlaika uzvareja:")
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
        #print("Pamatlaika uzvareja:")
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
              


    #print("Statistics:")
    # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[0].name+"', '"+str(tmp[0].PUN_TOT)+"', '"+str(tmp[0].USKPM)+"','"+str(tmp[0].ZSKPM)+"','"+str(tmp[0].UZSKPL)+"','"+str(tmp[0].ZSKPL)+"','"+str(tmp[0].IEGV)+"','"+str(tmp[0].ZAUV)+"','"+rinkis+"')") 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[1].name+"', '"+str(tmp[1].PUN_TOT)+"', '"+str(tmp[1].USKPM)+"','"+str(tmp[1].ZSKPM)+"','"+str(tmp[1].UZSKPL)+"','"+str(tmp[1].ZSKPL)+"','"+str(tmp[1].IEGV)+"','"+str(tmp[1].ZAUV)+"', '"+rinkis+"')") 
  conn.commit() 
  conn.close()
#ENDof my_function()

def my_function2(where):
  #print("Hello from a function")
  # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  # Creating a cursor object using the  
  # cursor() method 
  cursor = conn.cursor() 
  data3=cursor.execute("SELECT name,sum(PUN_TOT), sum(USKPM), sum(ZSKPM), sum(UZSKPL), sum(ZSKPL), sum(IEGV), sum(ZAUV) FROM TEAM "+where+" group by name order by sum(PUN_TOT) desc")
  print(cursor.fetchall())
  # Commit your changes in the database     
  conn.commit() 
  # Closing the connection 
  conn.close()

#END of my_function2()
def my_function3():
  #print("Hello from a function")
  # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  # Creating a cursor object using the  
  # cursor() method 
  cursor = conn.cursor() 
  data3=cursor.execute("SELECT * FROM PLAYER")
  #print(cursor.fetchall())
  # Commit your changes in the database     
  conn.commit() 
  # Closing the connection 
  conn.close()
#END of my_function3()
def my_function4(nr, iegv, rpsk):
  #print("Hello from a function")
  # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  # Creating a cursor object using the  
  # cursor() method 
  cursor = conn.cursor() 
  #data3=cursor.execute("SELECT * FROM PLAYER")
  data3=cursor.execute("UPDATE FROM PLAYER")

  #print(cursor.fetchall())
  # Commit your changes in the database     
  conn.commit() 
  # Closing the connection 
  conn.close()
#END of my_function4()
def addvarti_function4(nr):
  #print("Hello from a function")
  # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  # Creating a cursor object using the  
  # cursor() method 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" ")
  #data3=cursor.execute("UPDATE FROM PLAYER")

  print(cursor.fetchall())
  print("last:")
  for row in playerdata: 
    print(row) 
  #print(playerdata['NAME'])
  #print(playerdata[0])
  # Commit your changes in the database     
  conn.commit() 
  # Closing the connection 
  conn.close()
#END of my_function4()

#main
path="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLFirstRound/"
w1=" WHERE RINKIS='1.rinkis'"
print("1.rinkis")
for i in range (0,3):
  #print(i)
  my_function(i, path,'1.rinkis')
my_function2(w1)
print("2.rinkis")
path1="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLSecondRound/"
w2=" WHERE RINKIS='2.rinkis'"
for i in range (0,3):
  #print(i)
  my_function(i, path1,'2.rinkis')
my_function2(w2)
#w3=" WHERE RINKIS='1.rinkis' AND WHERE RINKIS='2.rinkis'"
#my_function2(w3)
print("1.un 2.rinkis")
my_function2("")

my_function3()
addvarti_function4(47)

#END of main



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

