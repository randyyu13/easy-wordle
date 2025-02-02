from db.base_dao import BaseDAO
from models.Word import Word

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
        self.execute(query)
        rows = self.fetch_all()
        return [Word(**row) for row in rows]

    def set_word_of_the_day(self, date):
        # Check if the date already exists in the dateUsed column
        query_check = "SELECT id, word FROM wordsTbl WHERE dateUsed = %s;"
        self.execute(query_check, (date,))
        existing_word = self.fetch_one()

        if existing_word:
            return {"message": f"A word is already set for {date}."}

        # Select a random word that hasn't been used
        query_select_random = "SELECT id, word FROM wordsTbl WHERE dateUsed IS NULL ORDER BY RANDOM() LIMIT 1;"
        self.execute(query_select_random)
        word_row = self.fetch_one()

        if not word_row:
            return {"message": "No available words to set as word of the day."}

        # Create a Word object and update using the existing method
        word = Word(
            id=word_row["id"],
            word=word_row["word"],
            was_used=True,   # Set wasUsed to True
            date_used=date   # Assign today's date
        )

        # Use the update_word method for abstraction
        self.update_word(word)

        return {"message": f"Word of the day set to '{word.word}' for {date}."}
    
    def get_word_of_the_day(self, date):
        # Query to get the word for the given date
        query = """
        SELECT 
            id, 
            word, 
            wasUsed AS was_used, 
            dateUsed AS date_used 
        FROM wordsTbl WHERE dateUsed = %s;
        """
        self.execute(query, (date,))
        word_row = self.fetch_one()

        if not word_row:
            return {"message": f"No word has been set for {date}."}

        # Convert database row to Pydantic model and return
        word = Word(**word_row)
        return word