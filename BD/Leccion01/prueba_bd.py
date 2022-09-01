import psycopg2

conexion = psycopg2.connect(  # Conectamos a la base de datos
    user='admin',
    password='admin',
    host='localhost',
    port='5432',
    database='test_db'
)
print(conexion)

cursor = conexion.cursor()  # Objeto que nos permite ejecutar sentencias SQL en PostgreSQL
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()

