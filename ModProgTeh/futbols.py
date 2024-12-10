
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
cursor_obj.execute(table)
table2 = """ CREATE TABLE PLAYER (
            NR INT,            
            KOM_NOS VARCHAR(255) NOT NULL,
            VARDS VARCHAR(255) NOT NULL,
            UZVARDS VARCHAR(255) NOT NULL,
            VARTI INT,
            PIESP INT,
            SODI INT 
         ); """  
cursor_obj.execute(table2) 
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

def my_function(i, path2,rinkis):
  tree = ET.parse(path2+'futbols'+str(i)+'.xml')
  root = tree.getroot()
  #print(root.tag)
  #print(root.attrib)
  tmp=[]
  nrpk=0
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
            addplayer_function(playernr,playerteam,personname,surname)
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
            #print("Vārtus iesita NR.="+vg.get("Nr"))
            #print("Vārtus iesta spēlētājs: "+komanda.get("Nosaukums"))
            addvarti_function4(vg.get("Nr"),komanda.get("Nosaukums"))#,
            for pie in vg.iter('P'):
              addpiesp_function5(pie.get("Nr"),komanda.get("Nosaukums"))
              #  print(p.get("Nr"))
    if (len(tmp)>1):
      #print("Ieliek zaudētie vārti:")
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
    # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[0].name+"', '"+str(tmp[0].PUN_TOT)+"', '"+str(tmp[0].USKPM)+"','"+str(tmp[0].ZSKPM)+"','"+str(tmp[0].UZSKPL)+"','"+str(tmp[0].ZSKPL)+"','"+str(tmp[0].IEGV)+"','"+str(tmp[0].ZAUV)+"','"+rinkis+"')") 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[1].name+"', '"+str(tmp[1].PUN_TOT)+"', '"+str(tmp[1].USKPM)+"','"+str(tmp[1].ZSKPM)+"','"+str(tmp[1].UZSKPL)+"','"+str(tmp[1].ZSKPL)+"','"+str(tmp[1].IEGV)+"','"+str(tmp[1].ZAUV)+"', '"+rinkis+"')") 
  conn.commit() 
  conn.close()
#ENDof my_function()

def my_function2(where):
  conn = sqlite3.connect('team.db') 
  # Creating a cursor object using the  
  # cursor() method 
  cursor = conn.cursor() 
  data3=cursor.execute("SELECT name,sum(PUN_TOT), sum(USKPM), sum(ZSKPM), sum(UZSKPL), sum(ZSKPL), sum(IEGV), sum(ZAUV) FROM TEAM "+where+" group by name order by sum(PUN_TOT) desc").fetchall()
  #print(data3)
  i=0
  print("Vpk KNOS PUN_TOT USKPM ZSKPM UZSKPL ZSKPL IEGV ZAUV")
  for row in data3:
    i+=1
    print(str(i)+" "+str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])+" "+str(row[6]))
  # Commit your changes in the database     
  print("")
  conn.commit() 
  # Closing the connection 
  conn.close()
#END of my_function2()

def my_function3():
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data3=cursor.execute("SELECT * FROM PLAYER")  
  conn.commit() 
  conn.close()
#END of my_function3()

def my_function4(nr, iegv, rpsk):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data3=cursor.execute("UPDATE FROM PLAYER")
  conn.commit() 
  conn.close()
#END of my_function4()

def addplayer_function(nr, team, name, surname):#playernr,playerteam,personname,surname)
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT DISTINCT * FROM PLAYER WHERE NR="+str(nr)+" AND VARDS='"+name+"' AND UZVARDS='"+surname+"' AND KOM_NOS='"+team+"'").fetchall()
  if(len(playerdata)==0):
    cursor.execute("INSERT INTO PLAYER VALUES ("+str(nr)+",'"+team+"','"+name+"','"+surname+"',0,0,0)")
  conn.commit() 
  conn.close()
#END of addplayer_function

def addvarti_function4(nr, team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  varti=0
  for row in playerdata: 
    varti=row[4]
  cursor.execute("UPDATE PLAYER SET VARTI = "+str(varti+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  conn.commit() 
  conn.close()
#END of my_function4()

def addpiesp_function5(nr, team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  piesp=0
  for row in playerdata: 
    piesp=row[5]
  cursor.execute("UPDATE PLAYER SET PIESP = "+str(piesp+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()  
  conn.commit() 
  conn.close()
#END of my_function5()
def my_function6(nr):#Print player info
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" ")
  print(cursor.fetchall())
  conn.commit() 
  conn.close()
#END of my_function6()
def addsodi_function7(nr):
#print("Hello from a function")
  # Connecting to sqlite 
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" ").fetchall()
  sodi=0
  for row in playerdata: 
    #print(row[6])
    sodi=row[6]#sodi
  #print("Varti="+str(varti))
  cursor.execute("UPDATE PLAYER SET SODI = "+str(sodi+1)+" WHERE NR = "+str(nr)).fetchall() 
  conn.commit() 
  # Closing the connection 
  conn.close()
#END of my_function7()
def my_function8():
#print("Hello from a function")
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data5=cursor.execute("SELECT VARDS, UZVARDS, NR , KOM_NOS, VARTI, PIESP FROM PLAYER ORDER BY VARTI DESC, PIESP DESC LIMIT 100").fetchall()
  i=0
  print("Turnira 100 rezultativakie speletaji")
  print("Vpk Vards Uzvards Nr Kom_Nos GVSK RPSK")
  for row in data5:
    i+=1
    print(str(i)+" "+str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5]))
  conn.commit() 
  conn.close()
#END of my_function8()

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
print("1.un 2.rinkis")
my_function2("")
my_function3()
print("   ")
#addvarti_function4(47)
#addvarti_function4(47)

#addvarti_function4(147)


#Testing
#my_function6(55)
#addsodi_function7(55)
#my_function6(55)
my_function8()
#print("    ")
#my_function6(39)
#my_function6(24)
#my_function6(34)


#END of main


