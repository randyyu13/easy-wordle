from api.db.connection import Database
from api.db.words_tbl_dao import WordDAO
from api.models.Word import Word
from wordfreq import top_n_list
from nltk.corpus import words
import nltk

# Initialize the database connection pool
Database.initialize(
    host="localhost",       # Must match DBeaver's "Host" field
    database="mydb",        # Must match DBeaver's "Database" field
    user="myuser",          # Must match DBeaver's "Username"
    password="mypassword", # Must match the password you set in DBeaver
    port=5432               # Must match DBeaver's "Port"
)

word_dao = WordDAO()

nltk.download('words')
english_words = set(words.words())

five_letter_words = [
    word for word in top_n_list('en', 200000)
    if len(word) == 5 and word.lower() in english_words
]

for word in five_letter_words[:100000]:
    new_word = Word(id=None, word=word, was_used=False, date_used=None)
    word_dao.insert_word(new_word)

# # Write to a text file
# with open("top_100k_five_letter_words.txt", "w") as f:
#     for word in five_letter_words[:100000]:
#         new_word = Word(id=None, word=word, was_used=False, date_used=None)
#         word_dao.insert_word(new_word)
#         # f.write(f"{word}\n")
