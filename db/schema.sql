
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

CREATE TABLE historial
(
gen INTEGER PRIMARY KEY,
parameters TEXT NOT NULL,
elo REAL NOT NULL
);

INSERT INTO stats (num_comparisons)
VALUES (0);
