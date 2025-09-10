from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = "zona_fit_db"
    USERNAME = "root"
    PASSWORD = "admin"
    HOST = "localhost"
    DB_PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener el pool: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    # Creacion del objeto pool
    #pool = Conexion.obtener_pool()
    #print(pool)

    # Obtener un objeto conexion
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    Conexion.liberar_conexion(cnx1)