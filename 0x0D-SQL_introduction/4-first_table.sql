-- Creates a table called first_table in the current database in MySQL server.
-- The database name will be passed as an argument of the mysql command
-- first_table description:
-- id INT
-- name VARCHAR(256)
-- if the table first_table already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
