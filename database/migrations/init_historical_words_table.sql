CREATE TABLE wordsHistoricalTbl (
    eventDate DATE NOT NULL PRIMARY KEY,  -- Make event_date the primary key
    eventId SERIAL NOT NULL UNIQUE,      -- Ensure event_id is unique
    word VARCHAR(5) NOT NULL              -- Word must be present
);