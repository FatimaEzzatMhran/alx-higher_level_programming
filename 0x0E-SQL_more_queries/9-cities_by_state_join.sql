-- lists all cities contained in the dtabase hbtn_0d_usa
-- Each record should display cities.id, cities.name, states.name
-- Can only use SELECT statment once
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
