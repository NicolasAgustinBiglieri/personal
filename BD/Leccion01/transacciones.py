import psycopg2 as bd

conexion = bd.connect(  # Conectamos a la base de datos
    user='postgres',
    password='admin',
    host='localhost',
    port='5433',
    database='test_db'
)
try:
    # conexion.autocommit = False  # Esto es así por default

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Carlos', 'Lara', 'clara@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    print('Termina la transacción, se hizo commit')
    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
