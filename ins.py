import pymssql
conn = pymssql.connect(server="pokestats.database.windows.net", user="PokeAdmin@pokestats", password="P0k3m0ns", database="PokeStatsDB")
cursor = conn.cursor()
cursor.execute("INSERT INTO pokeTABLE (Id, name, type1, type2, HP, ATK, DEF, SpA, SpD, Speed) VALUES ('1', 'Bulbasaur', 'Grass', 'Poison', 45, 49, 49, 65, 65, 45)")
cursor.execute("INSERT INTO pokeTABLE (Id, name, type1, type2, HP, ATK, DEF, SpA, SpD, Speed) VALUES ('2', 'Ivysaur', 'Grass', 'Poison', 60, 62, 63, 80, 80, 60)")
conn.commit()

cursor.execute("SELECT * FROM pokeTABLE")
row = cursor.fetchone()
while row:
	print str(row[0]) + ", " + row[1] + ", " + row[2] + ", " + row[3]
	row = cursor.fetchone()	
