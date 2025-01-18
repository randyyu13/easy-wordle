class Game:
    def __init__(self, id, word, user_id, guessed_letters, guessed_words):
        self.id = id
        self.word = word
        self.user_id = user_id
        self.guessed_letters = guessed_letters
        self.guessed_words = guessed_words
        