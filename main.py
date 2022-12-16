import sqlite3

# Acá creamos una conexión a la base de datos, puede estar previamente creada.
conn = sqlite3.connect("estudiantes.db")

c = conn.cursor()

# Con el execute() lo que vamos a hacer es crear una nueva Base, porque estudiantes.db
# no la teníamos creada. Luego, la comentamos para cuando ejecutemos de nuevo el script
# no nos genere una nueva tabla con el mismo nombre
# c.execute(
#     """ CREATE TABLE estudiantes (
#     nombre TEXT,
#     edad INTEGER,
#     estatura REAL
# )"""
# )

# c.execute("INSERT INTO estudiantes VALUES ('Fran', 28, 1.76)")

# El comando executemany() nos permite crear varias filas a partir de una lista
lista_estudiantes = [("Messi", 35, 1.69), ("Julian", 22, 1.75), ("Dibu", 28, 1.95)]

# c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", lista_estudiantes)

c.execute("SELECT * FROM estudiantes")
print(c.fetchall())

# Guardar avances, hacemos un commit
conn.commit()

# Cerrar conexión
conn.close()

# Con todos los pasos realizados hasta acá, ya tenemos creada nuestra nueva Base de Datos,
# lo único que nos falta ahora, va a ser llenarla!
