ALTER TABLE player_bios
ADD COLUMN position text;

UPDATE player_bios 
SET position = 'PF' 
WHERE id IN (SELECT player FROM new_table WHERE position = 'PF');

UPDATE player_bios 
SET position = 'PG' 
WHERE id IN (SELECT player FROM new_table WHERE position = 'PG');

UPDATE player_bios 
SET position = 'C' 
WHERE id IN (SELECT player FROM new_table WHERE position = 'C');

UPDATE player_bios 
SET position = 'SG/SF' 
WHERE id IN (SELECT player FROM new_table WHERE position = 'SG/SF');

SELECT firstname, lastname, position FROM player_bios LIMIT 5;