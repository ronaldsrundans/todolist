
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
            SODI INT,
            SPELUSK INT,
            SPELUSEC INT,
            KARTEDZE INT,
            KARTESAR INT,
            LOMA VARCHAR(5)
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
    self.laukuma=[]#Pamatsastāva numuri
    self.mainaNr1=[]#Spēlētāju numuri, kuri tiek nomainīti
    self.mainaNr2=[]#Spēlētāja numuri, kuri uzsāk spēli nomainītā spēlētāja vietā
    self.mainaT=[]#Maiņas laiks
    self.sodiNr=[]#Spēlētājiem sodi
#END of class Team

def readinputfile(i, filepath,rinkis): 
  tree = ET.parse(filepath+'futbols'+str(i)+'.xml')
  root = tree.getroot()
  tmp=[]
  nrpk=0
  endtime=""#laiks,kad bija pēdējie vārti
  for komanda in root.iter('Komanda'):
    tmp.append(Team(komanda.get("Nosaukums")))
    nrpk+=1
    uzlaukuma=[]
    for speletaji in komanda.iter('Speletaji'):
         for speletajs in speletaji.iter('Speletajs'):
            surname = speletajs.get ("Uzvards")
            personname = speletajs.get("Vards")
            playernr=speletajs.get("Nr")
            playerteam=tmp[nrpk-1].name
            loma=speletajs.get("Loma")
            addplayer(playernr,playerteam,personname,surname, loma)
    for mainas in komanda.iter('Mainas'):
      for maina in mainas.iter('Maina'):
        #print(maina.attrib)
        playernr2=maina.get("Nr2")
        uzlaukuma.append(playernr2)
        tmp[nrpk-1].mainaNr2.append(playernr2)
        playerteam=tmp[nrpk-1].name
        playernr1=maina.get("Nr1")
        tmp[nrpk-1].mainaNr1.append(playernr1)
        playertime=maina.get("Laiks")
        tmp[nrpk-1].mainaT.append(playertime)
        fieldtime=playertime.split(":")
        addTime(playernr2,playerteam, int(fieldtime[0])*60+int(fieldtime[1]))#WRONG TIME
    for pamatsastavs in komanda.iter('Pamatsastavs'):
      for speletajs in pamatsastavs.iter('Speletajs'):
        #print(maina.attrib)
        playernr=speletajs.get("Nr")
        uzlaukuma.append(playernr)
        tmp[nrpk-1].laukuma.append(playernr)
        #print(tmp[nrpk-1].laukuma)
    for sodi in komanda.iter('Sodi'):
        for sods in sodi.iter('Sods'):
            #print(sods.attrib)
            playernr=sods.get("Nr")
            sodstime=sods.get("Laiks")
            playerteam=tmp[nrpk-1].name
            if playernr in tmp[nrpk-1].sodiNr:
              addKarteSar(playernr,playerteam)
              tmp[nrpk-1].laukuma.remove(playernr)
              speleslaiks=sodstime.split(":")
              addTime(playernr,tmp[nrpk-1].name, (int(speleslaiks[0])*60)+int(speleslaiks[1]))
            else:
              addKarteDz(playernr,playerteam)
            addsodi(playernr,playerteam)
            
    for varti in komanda.iter('Varti'):
        for vg in varti.iter('VG'):
            goaltime = vg.get("Laiks").split(":")
            if (endtime < vg.get("Laiks")):
              endtime=vg.get("Laiks")
            if(int(goaltime[0])>59 and int(goaltime[1])>1):
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
    for j in uzlaukuma:
      addSpele(j,str(tmp[nrpk-1].name))
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
  print("ENDtime= "+endtime)
  speleslaiks=endtime.split(":")
  endtimesec=int(speleslaiks[0])*60+int(speleslaiks[1])
  
  print(tmp[0].mainaT)
  for i in range(2):
    for k1 in tmp[i].mainaNr1:
      print(k1)
      tmp[i].laukuma.remove(k1)
    c=0
    for k2 in tmp[i].mainaNr2:
      print(k2)     
      mainaTsec=tmp[i].mainaT[c].split(":")
      addTime(j,tmp[i].name, int(endtimesec)-int(60*mainaTsec[0]+mainaTsec[0])) 
      c+=1
    for j in tmp[i].laukuma:
      addTime(j,tmp[i].name, endtimesec)
      #pieskaita speles laikus

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

def addplayer(nr, team, name, surname, role):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT DISTINCT * FROM PLAYER WHERE NR="+str(nr)+" AND VARDS='"+name+"' AND UZVARDS='"+surname+"' AND KOM_NOS='"+team+"'").fetchall()
  if(len(playerdata)==0):
    cursor.execute("INSERT INTO PLAYER VALUES ("+str(nr)+",'"+team+"','"+name+"','"+surname+"',0,0,0,0,0,0,0, '"+role+"')")
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
  #END of myfunction())

def addSpele(nr,team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  speles=0
  for row in playerdata: 
    speles=row[7]#spelu sk
  cursor.execute("UPDATE PLAYER SET SPELUSK = "+str(speles+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall() 
  conn.commit() 
  conn.close()
  #END of addSpele()

def addTime(nr,team, time):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  timemin=0
  for row in playerdata: 
    timemin=row[8]#spelu LAIKS
  timemin=(timemin+time)
  cursor.execute("UPDATE PLAYER SET SPELUSEC = "+str(timemin+time)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall() 
  conn.commit() 
  conn.close()
  #END of addTime()

def addKarteDz(nr,team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  dzkarte=0
  for row in playerdata: 
    dzkarte=row[9]#spelu sk
  cursor.execute("UPDATE PLAYER SET SPELUSK = "+str(dzkarte+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall() 
  conn.commit() 
  conn.close()
  #END of addKarteDz()
def addKarteSar(nr,team):
  conn = sqlite3.connect('team.db') 
  cursor = conn.cursor() 
  playerdata=cursor.execute("SELECT * FROM PLAYER WHERE NR="+str(nr)+" AND KOM_NOS='"+team+"'").fetchall()
  dzkarte=0
  for row in playerdata: 
    dzkarte=row[9]#spelu sk
  cursor.execute("UPDATE PLAYER SET SPELUSK = "+str(dzkarte+1)+" WHERE NR = "+str(nr)+" AND KOM_NOS='"+team+"'").fetchall() 
  conn.commit() 
  conn.close()
#END of addKarteSar()




def mainTest():
  print("1.rinkis")
  #path="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLFirstRound/"
  path="XML_TestData/XMLFirstRound/"
  m1=" WHERE RINKIS='1.rinkis'"
  for i in range (0,3):
    readinputfile(i, path,'1.rinkis')
  teamStatistics(m1)

  print("2.rinkis")
  #path1="/home/ubuntu/Documents/ModProgrMet/PD2/XML_TestData/XMLSecondRound/"
  path1="XML_TestData/XMLSecondRound/"
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
  getPlayerInfo(9)
#END of mainTest
"""visu vienas komandas spēlētāju apkopojošā statistika, par katru spēlētāju norādot tā numuru, 
vārdu, uzvārdu, nospēlēto spēļu skaitu, nospēlēto spēļu skaits pamatsastāvā, nospēlētās minūtes, 
iesisto vārtu un rezultatīvo piespēļu skaits, saņemtās dzeltenās kartītes, saņemtās sarkanās kartītes. 
Spēlētājs ir spēlējis spēli, ja viņš tajā ir piedalījies kaut vienu sekundi. Atsevišķi jāveido vārtsargu 
statistika - nospēlēto spēļu skaits, ielaistie vārti, vidēji vienā spēlē ielaistie vārti."""
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


