from api.db.base_dao import BaseDAO
from api.models import Word

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