-- creates the database hbtn_0d_usa
-- creates the table cities in hbtn_0d_usa
-- cities description:
-- id INT, UNIQUE, auto generated, not null, primary key
-- state_id INT, not null, foreign key that references to id of the states table
-- name VARCHAR, not null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT UNIQUE NOT NULL PRIMARY KEY,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
