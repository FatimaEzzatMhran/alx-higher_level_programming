-- creates the database hbtn_0d_usa
-- creates the table states
-- states description:
-- id INT, auto generated, not null, primary key
-- name VARCHAR(256), not null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
