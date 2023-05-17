-- lists the number of records with the same score in the second_table
-- result should display the score
-- and the number of records for this score with the label number
-- sorted by the number of records (desc)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
