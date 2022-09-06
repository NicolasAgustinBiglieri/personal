import psycopg2

conexion = psycopg2.connect(  # Conectamos a la base de datos
    user='admin',
    password='admin',
    host='localhost',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:  # Objeto que nos permite ejecutar sentencias SQL en PostgreSQL
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(",")),)  # Split regresa lista, le sacamos las comas y convertimos en tupla
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
