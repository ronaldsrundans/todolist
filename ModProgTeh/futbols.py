
import xml.etree.ElementTree as ET
# Connecting to sqlite
import sqlite3
# connection object
connection_obj = sqlite3.connect('team.db') 
# cursor object
cursor_obj = connection_obj.cursor() 
# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS TEAM")
cursor_obj.execute("DROP TABLE IF EXISTS PLAYER")
# Creating table
tableteam = """ CREATE TABLE TEAM (
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
cursor_obj.execute(tableteam)
tableplayer = """ CREATE TABLE PLAYER (
            NR INT,            
            KOM_NOS VARCHAR(255) NOT NULL,
            VARDS VARCHAR(255) NOT NULL,
            UZVARDS VARCHAR(255) NOT NULL,
            VARTI INT,
            PIESP INT,
            SODI INT 
         ); """  
cursor_obj.execute(tableplayer) 
# Close the connection
connection_obj.close()

class Team:
  def __init__(self, name):
    self.name = name  #Komandas nosaukums
    self.PUN_TOT=0      #Iegūto punktu skaits
    self.USKPM=0      #Uzvaru skaits pamatlaikā
    self.ZSKPM=0     #Zaudējumu skaits pamatlaikā
    self.UZSKPL=0      #Uzvaru skaits papildlaikā
    self.ZSKPL=0       #Zaudējumu skaits papildlaikā
    self.IEGV=0       #Iegūto vārtuu skaits
    self.ZAUV=0     #Zaudēto vārtu skaits
    self.vpm=0  #Iegūto vārtu skaits pamatlaikā (tikai šajā spēlē) - nosaka piešķirtos punktus
    self.vpl=0  #Iegūto vārtu skaits papildlaikā (tikai šajā spēlē) - nosaka piešķirtos punktus
#END of class Team

def readinputfile(i, filepath,rinkis): 
  tree = ET.parse(filepath+'futbols'+str(i)+'.xml')
  root = tree.getroot()
  tmp=[]
  nrpk=0
  for komanda in root.iter('Komanda'):
    tmp.append(Team(komanda.get("Nosaukums")))
    nrpk+=1
    for speletaji in komanda.iter('Speletaji'):
         for speletajs in speletaji.iter('Speletajs'):
            surname = speletajs.get ("Uzvards")
            personname = speletajs.get("Vards")
            playernr=speletajs.get("Nr")
            playerteam=tmp[nrpk-1].name
            addplayer(playernr,playerteam,personname,surname)
    for sodi in komanda.iter('Sodi'):
        for sods in sodi.iter('Sods'):
            #print(sods.attrib)
            playernr=sods.get("Nr")
            playerteam=tmp[nrpk-1].name
            addsodi(playernr,playerteam)
    for varti in komanda.iter('Varti'):
        for vg in varti.iter('VG'):
            a = vg.get("Laiks").split(":")
            if(int(a[0])>59 and int(a[1])>1):
              #print("Papildlaiks!")
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpl+=1
            else:
              #print("Pamatlaiks!")
              tmp[nrpk-1].IEGV+=1
              tmp[nrpk-1].vpm+=1
            #print("Vārtus iesta spēlētājs: "+komanda.get("Nosaukums"))
            addvarti(vg.get("Nr"),komanda.get("Nosaukums"))#,
            for pie in vg.iter('P'):
              addpiesp(pie.get("Nr"),komanda.get("Nosaukums"))
    if (len(tmp)>1):
      #print("Ieliek zaudētie vārti:")
      tmp[0].ZAUV+=(tmp[1].vpl+tmp[1].vpm )#saskaita vārtus gan pamatlaikā gan papildlaikā no otras komandas
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
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[0].name+"', '"+str(tmp[0].PUN_TOT)+"', '"+str(tmp[0].USKPM)+"','"+str(tmp[0].ZSKPM)+"','"+str(tmp[0].UZSKPL)+"','"+str(tmp[0].ZSKPL)+"','"+str(tmp[0].IEGV)+"','"+str(tmp[0].ZAUV)+"','"+rinkis+"')") 
  cursor.execute("INSERT INTO TEAM VALUES ('"+tmp[1].name+"', '"+str(tmp[1].PUN_TOT)+"', '"+str(tmp[1].USKPM)+"','"+str(tmp[1].ZSKPM)+"','"+str(tmp[1].UZSKPL)+"','"+str(tmp[1].ZSKPL)+"','"+str(tmp[1].IEGV)+"','"+str(tmp[1].ZAUV)+"', '"+rinkis+"')") 
  conn.commit() 
  conn.close()
#END of readinputfile()

def teamStatistics(where): #my_function2
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data3=cursor.execute("SELECT name,sum(PUN_TOT), sum(USKPM), sum(ZSKPM), sum(UZSKPL), sum(ZSKPL), sum(IEGV), sum(ZAUV) FROM TEAM "+where+" group by name order by sum(PUN_TOT) desc").fetchall()
  i=0
  print("Vpk KNOS PUN_TOT USKPM ZSKPM UZSKPL ZSKPL IEGV ZAUV")
  for row in data3:
    i+=1
    print(str(i)+" "+str(row[0])+"  "+str(row[1])+"  "+str(row[2])+"  "+str(row[3])+"  "+str(row[4])+"  "+str(row[5])+"  "+str(row[6]))
  print("")
  conn.commit() 
  conn.close()
#END of teamStatistics()

def addplayer(nr, team, name, surname):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT DISTINCT * FROM PLAYER WHERE NR="+str(nr)+" AND VARDS='"+name+"' AND UZVARDS='"+surname+"' AND KOM_NOS='"+team+"'").fetchall()
  if(len(playerdata)==0):
    cursor.execute("INSERT INTO PLAYER VALUES ("+str(nr)+",'"+team+"','"+name+"','"+surname+"',0,0,0)")
  conn.commit() 
  conn.close()
#END of addplayer

def addvarti(nr, team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  varti=0
  for row in playerdata: 
    varti=row[4]
  cursor.execute("UPDATE PLAYER SET VARTI = "+str(varti+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  conn.commit() 
  conn.close()
#END of addvarti()

def addpiesp(nr, team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  piesp=0
  for row in playerdata: 
    piesp=row[5]
  cursor.execute("UPDATE PLAYER SET PIESP = "+str(piesp+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()  
  conn.commit() 
  conn.close()
#END of addpiesp()

def getPlayerInfo(nr):#Print player info
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" ")
  print(cursor.fetchall())
  conn.commit() 
  conn.close()
#END of getPlayerInfo

def addsodi(nr, team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  sodi=0
  for row in playerdata: 
    sodi=row[6]#sodi
  cursor.execute("UPDATE PLAYER SET SODI = "+str(sodi+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall() 
  conn.commit() 
  conn.close()
#END of addsodi()

def playerStatistics():
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data5=cursor.execute("SELECT VARDS, UZVARDS, NR , KOM_NOS, VARTI, PIESP FROM PLAYER ORDER BY VARTI DESC, PIESP DESC LIMIT 10").fetchall()
  i=0
  print("Turnira 10 rezultativakie speletaji")
  print("Vpk Vards Uzvards Nr Kom_Nos GVSK RPSK")
  for row in data5:
    i+=1
    print(str(i)+" "+str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5]))
  conn.commit() 
  conn.close()
#END of playerStatistics()

def getRupjakie():
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  data5=cursor.execute("SELECT VARDS, UZVARDS, NR , KOM_NOS, SODI FROM PLAYER ORDER BY SODI DESC LIMIT 10").fetchall()
  i=0
  print("Turnira 10 rupjāmkie speletaji")
  print("Vpk Vards Uzvards Nr Kom_Nos Sodi")
  for row in data5:
    i+=1
    print(str(i)+" "+str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4]))
  conn.commit() 
  conn.close()
#END of getRupjakie()

def my_function():
  print("Hello")

def mainTest():
  print("1.rinkis")
  path="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLFirstRound/"
  m1=" WHERE RINKIS='1.rinkis'"
  for i in range (0,3):
    readinputfile(i, path,'1.rinkis')
  teamStatistics(m1)

  print("2.rinkis")
  path1="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLSecondRound/"
  m2=" WHERE RINKIS='2.rinkis'"
  for i in range (0,3):
    readinputfile(i, path1,'2.rinkis')
  teamStatistics(m2)

  print("1.un 2.rinkis")
  teamStatistics("")

  print("   ")
  playerStatistics()
  print("   ")
  getRupjakie()
#END of mainTest

def main():
  path="/home/ubuntu/Documents/ModProgrMet/PD2/"
  message=" WHERE RINKIS='1.rinkis'"
  #print("1.rinkis")
  for i in range (0,3):#faila nosaukums: futbols+ i .xml
    readinputfile(i, path,"")
  teamStatistics("")
  playerStatistics()
#END of main


mainTest()


