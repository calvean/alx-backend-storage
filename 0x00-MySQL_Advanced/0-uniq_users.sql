--SQL script that creates a table users
--    With these attributes:
--        id, integer, never null, auto increment and primary key
--        email, string (255 characters), never null and unique
--        name, string (255 characters)
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255)
);
