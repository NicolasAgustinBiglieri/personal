import psycopg2

conexion = psycopg2.connect(  # Conectamos a la base de datos
    user='postgres',
    password='admin',
    host='localhost',
    port='5433',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:  # Objeto que nos permite ejecutar sentencias SQL en PostgreSQL
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2),
            )
            cursor.executemany(sentencia, valores)  # Ejecutamos muchos registros pasando tupla de tuplas como 2do param
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
