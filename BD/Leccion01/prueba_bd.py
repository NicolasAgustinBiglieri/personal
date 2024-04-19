import psycopg2

conexion = psycopg2.connect(  # Conectamos a la base de datos
    user='postgres',
    password='admin',
    host='localhost',
    port='5433',
    database='test_db'
)
print(conexion)

cursor = conexion.cursor()  # Objeto que nos permite ejecutar sentencias SQL en PostgreSQL
sentencia = 'SELECT * FROM persona' # Cremos la sentencia
cursor.execute(sentencia) # Ejecutamos la sentencia
registros = cursor.fetchall() # Registramos los registros en una lista
print(registros)

cursor.close()
conexion.close()

