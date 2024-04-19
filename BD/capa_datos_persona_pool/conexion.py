from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5433"
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # Aprovechamos mejor los recursos si usamos "Pool de conexión" a la base de datos, y obtenemos conexiones desde el pool
    # en vez de crear una conexión cada vez que la necesitamos
    # Para lo cual creamos un pool de conexiones (ej: Para hasta 5 conexiones) 

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try: # SimpleConnectionPool, conexión básica
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT)
                log.debug(f'Conexión del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error('Ocurrió un error al obtener el pool: {e}')
                sys.exit
        else:
            return cls._pool

    # El método de obtenerConexion nos permite crear conexiones que se le solicitan al método obtenerPool
    # En caso de que no exista el pool, esta cadena de métodos lo crea y lo devuelve, en caso de que no exista, lo crea.
    @classmethod
    def obtenerConexion(cls): 
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión de objeto exitosa: {conexion}')
        return conexion
    

    # Creamos un método para liberar objetos de tipo conexión, para que se puedan reutilizar y se aproveche el pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    # Creamos método para cerrar todo el pool de conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
    conexion7 = Conexion.obtenerConexion()
    conexion8 = Conexion.obtenerConexion()