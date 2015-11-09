import pymssql
conn = pymssql.connect(server="pokestats.database.windows.net", user="PokeAdmin@pokestats", password="P0k3m0ns", database="PokeStatsDB")
cursor = conn.cursor()
cursor.execute("SELECT * FROM pokeTABLE")
row = cursor.fetchone()
while row:
	print str(row[0]) + ", " + row[1] + ", " + row[2] + ", " + row[3]
	row = cursor.fetchone()