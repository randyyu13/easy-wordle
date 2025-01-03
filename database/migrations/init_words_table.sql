CREATE TABLE wordsTbl (
    id SERIAL PRIMARY KEY,
    word VARCHAR(5) UNIQUE,
    wasUsed BOOLEAN,
    dateUsed DATE
)