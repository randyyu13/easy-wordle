from db.base_dao import BaseDAO
from models.Word import Word
from psycopg2.extras import RealDictCursor

class WordDAO(BaseDAO):
    def insert_word(self, word: Word):
        query = """
        INSERT INTO wordsTbl (word, wasUsed, dateUsed)
        VALUES (%s, %s, %s)
        ON CONFLICT (word) DO NOTHING;
        """
        self.execute(query, (word.word, word.was_used, word.date_used))

    def update_word(self, word: Word):
        query = """
        UPDATE wordsTbl
        SET wasUsed = %s, dateUsed = %s
        WHERE word = %s;
        """
        self.execute(query, (word.was_used, word.date_used, word.word))

    def get_all_words(self):
        query = """
        SELECT 
            id, 
            word, 
            wasUsed AS was_used, 
            dateUsed AS date_used 
        FROM wordsTbl;
        """
        rows = self.execute_and_fetch_all(query)
        return [Word(**row) for row in rows]
