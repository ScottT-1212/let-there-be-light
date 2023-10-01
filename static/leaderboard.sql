CREATE TABLE leaderboard (
    id INTEGER NOT NULL PRIMARY KEY,
    player_name TEXT NOT NULL,
    level_number INTEGER NOT NULL,
    score INTEGER NOT NULL,
    grid_size INTEGER,
    time TIME
);