-- lists all records of the second_table
-- Don't list rows without a name value
-- results should display the score, the name (in this order)
-- records should be listed by desc score
SELECT `score`, `name`
FROM `second_table`
HAVING `name` IS NOT NULL
ORDER BY `score` DESC;
