DROP TABLE IF EXISTS computers;
DROP TABLE IF EXISTS printers;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE computers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ram TEXT NOT NULL,
    cpu TEXT NOT NULL,
    hdd TEXT NOT NULL,
    location TEXT NOT NULL,
    install_date TEXT
);

CREATE TABLE printers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    cartridge TEXT NOT NULL,
    location TEXT NOT NULL,
    install_date TEXT
);


