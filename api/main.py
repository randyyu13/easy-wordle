import os
from fastapi import FastAPI, Depends
from db.connection import Database

from db.words_tbl_dao import WordDAO
from db.user_tbl_dao import UserDAO
from db.game_tbl_dao import GameDAO

from models.Word import Word
from models.User import User
from models.Game import Game

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

def get_user_dao():
    return UserDAO()

def get_game_dao():
    return GameDAO()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/all-words", response_model=List[Word])
def get_all_words(word_dao: WordDAO = Depends(get_word_dao)):
    words = word_dao.get_all_words()
    return words

# Need to modify these methods eventually to actually take in a date parameter because we need that info from client side
@app.get("/word-of-the-day", response_model=Union[Word, dict])
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

@app.post("/word-of-the-day")
def set_word_of_the_day(word_dao: WordDAO = Depends(get_word_dao)):
    """
    Endpoint to set today's word of the day.
    """
    today = date.today().isoformat()  # Get today's date as YYYY-MM-DD
    result = word_dao.set_word_of_the_day(today)
    return result

@app.post("/new-user")
def create_user(user_data: User, user_dao: UserDAO = Depends(get_user_dao)):
    """
    Endpoint to create a new user.
    """
    user_dao.insert_user(user_data)
    return {"message": "User created successfully"}

# @app.get("/is-real-word")
# def is_real_word(word: str, word_dao: WordDAO = Depends(get_word_dao)):
#     """
#     Endpoint to check if a word is real.
#     """
#     return word_dao.is_valid_word(word)

@app.post("/new-game")
def create_game(game_data: Game, game_dao: GameDAO = Depends(get_game_dao)):
    """
    Endpoint to create a new game.
    """
    game_dao.insert_game(game_data)
    return {"message": "Game created successfully"}

@app.get("/game-data")
def get_game_data(user_id: str, game_dao: GameDAO = Depends(get_game_dao)):
    """
    Endpoint to get game data by user id.
    """
    return game_dao.get_game_by_user_id(user_id)

@app.patch("/game-data")
def update_game_data(game_data: Game, game_dao: GameDAO = Depends(get_game_dao)):
    """
    Endpoint to update game data.
    """
    game_dao.upsert_game(game_data)
    return {"message": "Game updated successfully"}