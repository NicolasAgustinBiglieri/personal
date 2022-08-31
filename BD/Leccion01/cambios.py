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
            sentencia = 'UPDATE persona SET nombre = "Juan", apellido = "Perez" WHERE id_persona = 1'  # Parametro posicional o Placeholder
            #id_persona = input('Proporcione el valor id_persona ')  # Solicitamos 1 registro al usuario
            cursor.execute(sentencia)  # Agregamos el 2do param (placeholder) solicitado al usuario
            registros = cursor.fetchall()  # fetchall para todos los registros indicados, fetchone para solo 1
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()