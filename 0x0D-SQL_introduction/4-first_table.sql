-- creates a table called first_table in the current database in your MySQL server.
-- the table should have (id INT) and (name VARACHAR(256)
-- if table exists, script shouldn't fail
-- Don't use SELECT or SHOW
CREATE TABLE IF NOT EXISTS `first_table` (`id` INT, `name` VARCHAR(256));
