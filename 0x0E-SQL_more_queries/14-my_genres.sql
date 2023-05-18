-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- Use only one SELECT statement
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres m 
ON tv_genres.id = m.genre_id
INNER JOIN tv_shows s 
ON m.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY tv_genres.name ASC;
