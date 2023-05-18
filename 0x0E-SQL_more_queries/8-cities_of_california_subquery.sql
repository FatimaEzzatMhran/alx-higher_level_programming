-- lists all the cities of California that can be found in hbtn_0d_usa datbase
-- states table contains only one record name = California
-- Results must be sorted in ascending order by cities.id
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
	SELECT `id`
	From `states`
	WHERE `name` = "California")
ORDER BY `id`;
