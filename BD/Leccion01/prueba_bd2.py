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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Parametro posicional o Placeholder
            id_persona = input('Proporcione el valor id_persona: ')  # Solicitamos 1 registro al usuario
            cursor.execute(sentencia, (id_persona,))  # Agregamos el 2do param (placeholder) solicitado al usuario
            registros = cursor.fetchone()  # fetchall para todos los registros indicados, fetchone para solo 1
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

