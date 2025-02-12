CREATE TABLE gameDataTbl (
    id SERIAL PRIMARY KEY,
    word VARCHAR(5),
    userId VARCHAR(100) UNIQUE,
    guessedLetters CHAR(1)[],
    guessedWords CHAR(5)[]
)