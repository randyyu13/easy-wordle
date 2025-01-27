import os
from fastapi import FastAPI, Depends
from db.connection import Database
from db.words_tbl_dao import WordDAO
from models.Word import Word
from datetime import date
from typing import List
from typing import Union


app = FastAPI()

# Get DB credentials from environment variables
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "mydb")
db_user = os.getenv("DB_USER", "myuser")
db_password = os.getenv("DB_PASSWORD", "mypassword")

# Initialize database connection
Database.initialize(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=int(db_port)
)

# Dependency to get the WordDAO instance
def get_word_dao():
    return WordDAO()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/allwords", response_model=List[Word])
def get_all_words(word_dao: WordDAO = Depends(get_word_dao)):
    words = word_dao.get_all_words()
    return words

# Need to modify these methods eventually to actually take in a date parameter because we need that info from client side
@app.get("/wotd", response_model=Union[Word, dict])
def get_word_of_the_day(word_dao: WordDAO = Depends(get_word_dao)):
    """
    Endpoint to retrieve today's word of the day.
    """
    today = date.today().isoformat()  # Get today's date as YYYY-MM-DD
    result = word_dao.get_word_of_the_day(today)
    if isinstance(result, dict):
        print("is dict response")
        return {"message": result["message"]}
    return result

@app.post("/wotd")
def set_word_of_the_day(word_dao: WordDAO = Depends(get_word_dao)):
    """
    Endpoint to set today's word of the day.
    """
    today = date.today().isoformat()  # Get today's date as YYYY-MM-DD
    result = word_dao.set_word_of_the_day(today)
    return result