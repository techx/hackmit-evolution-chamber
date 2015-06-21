
CREATE TABLE current
(
id INTEGER PRIMARY KEY,
parameters TEXT NOT NULL,
elo REAL NOT NULL
);

CREATE TABLE stats
(
num_comparisons INTEGER NOT NULL
);

CREATE TABLE historical
(
gen INTEGER PRIMARY KEY,
parameters TEXT NOT NULL,
elo REAL NOT NULL
);

CREATE TABLE decisions
(
id INTEGER PRIMARY KEY,
winner_id INTEGER NOT NULL,
winner_parameters TEXT NOT NULL,
loser_id INTEGER NOT NULL,
loser_parameters TEXT NOT NULL
);

INSERT INTO stats (num_comparisons)
VALUES (0);
