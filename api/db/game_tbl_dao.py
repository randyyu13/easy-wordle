from db.base_dao import BaseDAO
from models.Game import Game

class GameDAO(BaseDAO):
    def insert_game(self, game: Game):
        """
        Inserts a new game into the database.
        """
        query = """
        INSERT INTO gameDataTbl (word, userId, guessedLetters, guessedWords)
        VALUES (%s, %s, %s, %s);
        """
        self.execute(
            query,
            (
                game.word,
                game.user_id,
                game.guessed_letters,
                game.guessed_words,
            ),
        )
        self.connection.commit()
        self.close()

    def upsert_game(self, game: Game):
        """
        Inserts or updates a game in the database (upsert).
        """
        query = """
        INSERT INTO gameDataTbl (word, userId, guessedLetters, guessedWords)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (userId) 
        DO UPDATE SET 
            word = EXCLUDED.word,
            guessedLetters = EXCLUDED.guessedLetters,
            guessedWords = EXCLUDED.guessedWords;
        """
        self.execute(
            query,
            (
                game.word,
                game.user_id,
                game.guessed_letters,
                game.guessed_words,
            ),
        )
        self.connection.commit()
        self.close()

    def get_game_by_user_id(self, user_id: str) -> Game:
        """
        Retrieves a game by user_id.
        """
        query = """
        SELECT id, word, userId, guessedLetters, guessedWords
        FROM gameDataTbl
        WHERE userId = %s;
        """
        self.execute(query, (user_id,))
        row = self.fetch_one()
        self.close()
        if row:
            return Game(
                id=row['id'],
                word=row['word'],
                user_id=row['userid'],
                guessed_letters=row['guessedletters'],
                guessed_words=row['guessedwords']
            )
        return None
    