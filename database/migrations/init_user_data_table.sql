CREATE TABLE usersTbl (
    id SERIAL PRIMARY KEY,
    isGuest BOOLEAN,
    guestId VARCHAR(100) UNIQUE,
    username VARCHAR(100) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password CHAR(60)
);