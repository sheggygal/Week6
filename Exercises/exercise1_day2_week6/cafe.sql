-- Database: cafe

-- DROP DATABASE IF EXISTS cafe;

CREATE DATABASE cafe
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Israel.1251'
    LC_CTYPE = 'English_Israel.1251'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);
