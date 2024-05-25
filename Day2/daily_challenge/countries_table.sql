-- Database: countries

-- DROP DATABASE IF EXISTS countries;

CREATE DATABASE countries
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Israel.1251'
    LC_CTYPE = 'English_Israel.1251'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE Countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capital VARCHAR(100),
    flag TEXT,
    subregion VARCHAR(100),
    population BIGINT
);

SELECT*
From Countries