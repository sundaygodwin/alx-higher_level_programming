-- Script: Lists all records of the table second_table.
-- Records are ordered by descending score.
USE hbtn_0c_0;
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
