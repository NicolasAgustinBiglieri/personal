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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
            )
            cursor.executemany(sentencia, valores)  # Ejecutamos muchos registros pasando tupla de tuplas como 2do param
            # conexion.commit()  # commit() guarda los cambios en la base de datos, pero al usar with se guarda automaticamente
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

