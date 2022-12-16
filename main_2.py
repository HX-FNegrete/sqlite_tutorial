import sqlite3

connection = sqlite3.connect("gta.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE gta (release_year INTEGER, release_name TEXT, city TEXT)")

release_list = [
    (1997, "GTA", "state of New Guernsey"),
    (1999, "GTA 2", "Anywhere, USA"),
    (2001, "GTA III", "Liberty City"),
    (2002, "GTA Vice City", "Vice City"),
    (2004, "GTA San Andreas", "state of San Andreas"),
    (2008, "GTA IV", "Liberty City"),
    (2013, "GTA V", "Los Santos"),
]

cursor.executemany("Insert into gta values (?, ?, ?)", release_list)

cursor.execute("SELECT * FROM gta")
print(cursor.fetchall())

connection.commit()

connection.close()
