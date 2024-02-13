CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    password TEXT
    );

CREATE TABLE sheet_collection (
    id SERIAL PRIMARY KEY,
    name TEXT,
    type TEXT
);
