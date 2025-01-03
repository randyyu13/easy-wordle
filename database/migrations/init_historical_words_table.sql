CREATE TABLE wordsHistoricalTbl (
    event_date DATE,
    event_time TIME,
    event_id SERIAL,
    word VARCHAR(5),
    PRIMARY KEY (event_date, event_time, event_id)
);