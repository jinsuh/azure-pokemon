import pymssql
conn = pymssql.connect(server="pokestats.database.windows.net", user="PokeAdmin@pokestats", password="P0k3m0ns", database="PokeStatsDB")
cursor = conn.cursor()
name = 'Bulbasaur'
cursor.execute("INSERT INTO pokeTABLE VALUES (%s, %s, %s, %s, %d, %d, %d, %d, %d, %d)", ('1a', name, 'Grass', 'Poison', 45, 49, 49, 65, 65, 45))
name = 'Ivysaur'
cursor.execute("INSERT INTO pokeTABLE VALUES (%s, %s, %s, %s, %d, %d, %d, %d, %d, %d)", ('2', name, 'Grass', 'Poison', 45, 49, 49, 65, 65, 9000))
conn.commit()

cursor.execute("SELECT * FROM pokeTABLE")
row = cursor.fetchone()
while row:
	print str(row[0]) + ", " + row[1] + ", " + row[2] + ", " + row[3]
	row = cursor.fetchone()	
