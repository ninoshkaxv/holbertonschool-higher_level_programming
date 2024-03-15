-- This script creates a table second_table in the database hbtn_0c_0 in MySQL server and add multiple rows

CREATE TABLE IF NOT EXISTS second_table (
  ID INT,
  NAME VARCHAR(256),
  SCORE INT
  );
  INSERT INTO
    second_table
  VALUES
    (1, "Jhon", 10)
    (2, "Alex", 3)
    (3, "Bob", 14)
    (4, "George", 8);


