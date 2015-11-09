import requests
import pymssql
from bs4 import BeautifulSoup

#Exceptions
def isException(name):
	return name=="Deoxys" or name=="Wormadam" or name=="Shaymin" or name=="Darmanitan" or name=="Tornadus" or name=="Thundurus" or name=="Landorus" or name=="Keldeo" or name=="Meloetta" or name=="Meowstic" or name=="Aegislash" or name=="Pumpkaboo" or name=="Gourgeist" or name=="Hoopa" or name=="Giratina"

def addToName(name, mega_name):
	if (mega_name == ""):
		return name
	elif isException(name) and (name != "Hoopa"):
		return name + ": " + mega_name
	else:
		return mega_name

page = requests.get('http://pokemondb.net/pokedex/all')
page = BeautifulSoup(page.text, "lxml")

#db connection
#conn = pymssql.connect(server="pokestats.database.windows.net", user="PokeAdmin@pokestats", password="P0k3m0ns", database="PokeStatsDB")
#cursor = conn.cursor()

pokemonList = page.find('div', attrs={'class', 'colset'}).div.tbody.find_all('tr')

altCount = 1
checkDupName = ""
for pokemon in pokemonList:
	count = 0
	fields = pokemon.find_all('td')
	for field in fields:
		if (count == 0):
			numID = field.text.strip()
		elif (count == 1):
			name = field.a.text.strip()
			if (name == checkDupName):
				numID = numID + "-" + str(altCount)
				altCount += 1
			else:
				checkDupName = name
				altCount = 1
			altNameField = field.small
			if (altNameField== None):
				altName = ""
			else:
				altName = altNameField.text.strip()
			# name = field.text.strip()
		elif (count == 2):
			typeFields = field.find_all('a')
			type1 = typeFields[0].text.strip()
			if (len(typeFields) == 2):
				type2 = typeFields[1].text.strip()
			else:
				type2 = ""
		elif (count == 4):
			HP = field.text.strip()
		elif (count == 5):
			ATK = field.text.strip()
		elif (count == 6):
			DEF = field.text.strip()
		elif (count == 7):
			SpA = field.text.strip()
		elif (count == 8):
			SpD = field.text.strip()
		elif (count == 9):
			Speed = field.text.strip()
		count += 1
	name = addToName(name, altName)
	print numID, name, type1, type2, HP, ATK, DEF, SpA, SpD, Speed
		# print field.text.strip()
	# print numID
	#cursor.execute("INSERT INTO pokeTABLE (Id, name, type1, type2, HP, ATK, DEF, SpA, SpD, Speed) VALUES (" + numID + ", " + name + ", '', 'Poison', 45, 49, 49, 65, 65, 45)")
	#conn.commit()
	#print numID + ", " + name + ", " + hp + ", " + attack + ", " + defend + ", " + spa + ", " + spd + ", " + speed
