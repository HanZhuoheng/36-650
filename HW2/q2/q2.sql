DROP TABLE rdata;

CREATE TABLE rdata (
id SERIAL PRIMARY KEY,
a varchar(5) UNIQUE NOT NULL,
b varchar(5) UNIQUE NOT NULL,
moment date DEFAULT '2020-01-01',
x REAL CHECK (x > 0)
);

SELECT * FROM rdata;