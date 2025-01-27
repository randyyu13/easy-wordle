from pydantic import BaseModel
from datetime import date
from typing import Optional

class HistoricalWord(BaseModel):
    event_date: date  # Ensures correct date format
    event_id: Optional[int]  # ID might not be provided initially
    word: str