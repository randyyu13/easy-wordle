import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import pool

class Database:
    _connection_pool = None

    @staticmethod
    def initialize(**kwargs):
        Database._connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10, cursor_factory=RealDictCursor, **kwargs
        )

    @staticmethod
    def get_connection():
        return Database._connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database._connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database._connection_pool.closeall()