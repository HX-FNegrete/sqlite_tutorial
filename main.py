import sqlite3

# Acá creamos una conexión a la base de datos, puede estar previamente creada.
conn = sqlite3.connect("estudiantes.db")

c = conn.cursor()

# Con el execute() lo que vamos a hacer es crear una nueva Base, porque estudiantes.db
# no la teníamos creada.
c.execute(
    """ CREATE TABLE estudiantes (
    nombre TEXT, 
    edad INTEGER,
    estatura REAL
)"""
)

# Guardar avances, hacemos un commit
conn.commit()

# Cerrar conexión
conn.close()

# Con todos los pasos realizados hasta acá, ya tenemos creada nuestra nueva Base de Datos,
# lo único que nos falta ahora, va a ser llenarla!
