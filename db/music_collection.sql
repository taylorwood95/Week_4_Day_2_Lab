DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT

);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    release_year INT,
    genre VARCHAR(255)
);