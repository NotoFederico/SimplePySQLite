import sqlite3

connection = sqlite3.connect("DB1.db")
cursor = connection.cursor()
# Creación de la base de datos con campos de nombre, edad y sexo
#cursor.execute("CREATE TABLE USERS(NAME VARCHAR(50), AGE INTEGER, GENDER VARCHAR(50))")

# INSERT
"""
cursor.execute("INSERT INTO USERS VALUES('Federico',27,'male') ")
cursor.execute("INSERT INTO USERS VALUES('Martin',33,'male') ")
cursor.execute("INSERT INTO USERS VALUES('Victoria',25,'female') ")
cursor.execute("INSERT INTO USERS VALUES('Sandra',45,'female') ")
connection.commit()
"""

# Como acceder a los campos de la base de datos
"""
cursor.execute("SELECT * FROM USERS")
user = cursor.fetchone() # muestra el primer registro
user = cursor.fetchall() # muestra a todos los registros
for iterator in user:
    print(iterator)
"""

# Otra manera de agregar entradas
"""
regs = [
    ('Vittoria', 21, 'female'),
    ('Blas', 60, 'male'),
    ('Oriana', 24, 'female')
]
cursor.executemany("INSERT INTO USERS VALUES(?,?,?)",regs)
connection.commit()
"""

#Vamos a crear otra base de datos, esta vez de productos
# Creación de la base de datos con campos de nombre, edad y sexo

connection = sqlite3.connect(("Products.db"))
cursor = connection.cursor()
"""
# no pueden repetirse registros con el mismo "CODE"
cursor.execute("CREATE TABLE PRODUCTS(CODE VARCHAR(10) PRIMARY KEY, NAME VARCHAR(40), SECTION VARCHAR(20))")
regs = [
    ('AR01', 'Transistores', 'Electrónica'),
    ('AR02', 'Resistores', 'Electrónica'),
    ('AR03', 'Capacitores', 'Electrónica'),
    ('AR04', 'Amp. operacionales', 'Electrónica'),
    ('AR05', 'Inductores', 'Electrónica'),
    ('AR06', 'Switches', 'Ferretería')
]
cursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?)",regs)
connection.commit()
# Nota de color
# Si se usa AUTOINCREMENT puede obviarse el primer campo "codigo" para ser reemplazado por
# una sucesion incremental numerica en cada registro ingresado
"""
cursor.execute('UPDATE PRODUCTS SET SECTION ="Items de electrónica" WHERE SECTION = "Electrónica"')
cursor.execute('DELETE FROM PRODUCTS WHERE SECTION = "Ferretería"')
cursor.execute('SELECT * FROM PRODUCTS WHERE SECTION = "Ferretería" ORDER BY NAME DESC')
cursor.execute('SELECT * FROM PRODUCTS ORDER BY NAME ASC')
connection.commit()

filteredPrint = cursor.fetchall()
for iterator in filteredPrint:
    print(iterator)

connection.close()