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

CREATE TABLE sheet (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES sheet_collection,
    name TEXT,
    composer TEXT,
    writer TEXT,
    arranger TEXT,
    creator TEXT,
    artist TEXT
);
