import xml.etree.ElementTree as ET

class Team:
  def __init__(self, name):
    self.name = name
    self.win=0
    self.lose=0
    self.punkti=0
    self.varti=0
    self.pvarti=0
    self.PUN_TOT=0      
    self.USKPM=0      
    self.ZSKPM=0     
    self.UZSKPL=0      
    self.ZSKPL=0       
    self.IEGV=0       
    self.ZAUV=0


for i in range (1):
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
              tmp[nrpk-1].UZSKPL+=1
            else:
              print("Pamatlaiks!")
              tmp[nrpk-1].USKPM+=1
            #vgarr.append(vg.get("Laiks"))
    print("Statistics:")
    print("Statistics:")

  for x in vgarr:
    print(x)
print("TMP:  ")
for y in tmp:
  print(y.name)
  print(y.UZSKPL)
  print(y.USKPM)
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
