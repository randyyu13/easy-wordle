from pydantic import BaseModel
from typing import Optional
from datetime import date

class Word(BaseModel):
    id: Optional[int] = None
    word: str
    was_used: bool
    date_used: Optional[date] = None