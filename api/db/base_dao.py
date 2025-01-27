from db.connection import Database

class BaseDAO:
    def __init__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()

    def close(self):
        """Closes the cursor and returns the connection to the pool."""
        self.cursor.close()
        Database.return_connection(self.connection)

    def execute(self, query, params=None):
        """Executes a query with optional parameters."""
        self.cursor.execute(query, params or [])
        self.connection.commit()

    def fetch_all(self):
        """Fetch all rows from the last executed query."""
        return self.cursor.fetchall()

    def fetch_one(self):
        """Fetch a single row from the last executed query."""
        return self.cursor.fetchone()

    def execute_and_fetch_all(self, query, params=None):
        """Combines execute and fetch_all in one step."""
        self.execute(query, params)
        return self.fetch_all()