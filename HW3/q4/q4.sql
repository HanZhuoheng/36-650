CREATE TABLE new_table(
	 player integer references more_player_stats,
	 prl numeric,
	 position text
);
 
INSERT into new_table (SELECT id, round(per-67*va/(gp*minutes),1) AS prl FROM more_player_stats);

UPDATE new_table
SET position = 'PF'
WHERE prl >= 11.3;

UPDATE new_table
SET position = 'PG'
WHERE prl >= 10.8 and prl < 11.3;

UPDATE new_table
SET position = 'C'
WHERE prl >= 10.6 and prl < 10.8;

UPDATE new_table
SET position = 'SG/SF'
WHERE prl >= 0 and prl < 10.6;

SELECT * FROM new_table LIMIT 5