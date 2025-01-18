from api.db.connection import Database

class BaseDAO:
    def __init__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        Database.return_connection(self.connection)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or [])
        self.connection.commit()

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()