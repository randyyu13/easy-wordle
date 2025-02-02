from pydantic import BaseModel
from typing import Optional, List

class Game(BaseModel):
    id: Optional[int]  # ID might not be provided initially
    word: str
    user_id: str
    guessed_letters: List[str]  # List of single-character guessed letters
    guessed_words: List[str]  # List of guessed words (5-letter words)
