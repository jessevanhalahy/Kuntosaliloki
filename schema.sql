CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    category_id INTEGER REFERENCES categories,
    name TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises,
    user_id INTEGER REFERENCES users,
    content TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);