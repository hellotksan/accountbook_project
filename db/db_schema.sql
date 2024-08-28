DROP DATABASE IF EXISTS accountbook;

CREATE DATABASE accountbook;

USE accountbook

DROP TABLE IF EXISTS accountbooks;

CREATE TABLE accountbooks (
    id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    type VARCHAR(100) NOT NULL,
    breakdown VARCHAR(100) NOT NULL,
    price INT NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);