from db.base_dao import BaseDAO
from models.HistoricalWord import HistoricalWord

class HistoricalWordsDAO(BaseDAO):
    def upsert_historical_word(self, historical_word: HistoricalWord):
        """
        Inserts or updates a historical word for a given date.
        """
        query = """
        INSERT INTO wordsHistoricalTbl (event_date, word)
        VALUES (%s, %s)
        ON CONFLICT (event_date)
        DO UPDATE SET word = EXCLUDED.word
        RETURNING event_id;
        """
        self.execute(
            query,
            (
                historical_word.event_date,
                historical_word.word,
            ),
        )
        historical_word.event_id = self.fetch_one()[0]  # Set the generated or existing event_id
        self.connection.commit()

    def get_historical_word_by_date(self, event_date: str) -> HistoricalWord:
        """
        Retrieves the historical word for a given event_date.
        """
        query = """
        SELECT event_date, event_id, word
        FROM wordsHistoricalTbl
        WHERE event_date = %s;
        """
        self.execute(query, (event_date,))
        row = self.fetch_one()
        return HistoricalWord(*row) if row else None