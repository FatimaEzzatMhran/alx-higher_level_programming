-- create database hbtn_0d_2 and if it exists script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- create user user_0d_2 and set password to user_0d_2_pwd
-- If user exists, script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- user_0d_2 shold have only SELECT privileges in the database hbtn_0d_2
GRANT SELECT ON `hbtb_0d_2`.*
TO 'user_0d_2'@'localhost';
