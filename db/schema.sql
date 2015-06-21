
CREATE TABLE current
(
id INTEGER PRIMARY KEY,
parameters TEXT NOT NULL,
elo REAL NOT NULL
);

CREATE TABLE stats
(
num_decisions INTEGER NOT NULL
);

CREATE TABLE historial
(
gen INTEGER PRIMARY KEY,
parameters TEXT NOT NULL,
elo REAL NOT NULL
);

INSERT INTO stats (num_decisions)
VALUES (0);
