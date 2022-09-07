import psycopg2 as bd

conexion = bd.connect(  # Conectamos a la base de datos
    user='admin',
    password='admin',
    host='localhost',
    port='5432',
    database='test_db'
)
try:
    # con with se realizan automaticamente el autocommit = false, el commit si no hay error,
    # el rollback si hay error y el close del cursor
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
print('Termina la transacción, se hizo commit')
