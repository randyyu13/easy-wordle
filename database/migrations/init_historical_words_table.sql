CREATE TABLE wordsHistoricalTbl (
    event_date DATE NOT NULL PRIMARY KEY,  -- Make event_date the primary key
    event_id SERIAL NOT NULL UNIQUE,      -- Ensure event_id is unique
    word VARCHAR(5) NOT NULL              -- Word must be present
);