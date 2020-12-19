CREATE DATABASE liborg;
USE liborg;

CREATE TABLE users(
    userid INT NOT NULL,
    useremail varchar(255) NOT NULL,
    userpasswd VARCHAR(255) NOT NULL,
    PRIMARY KEY (userid)
);

CREATE TABLE books(
    bookid INT NOT NULL,
    tittle varchar(255) NOT NULL,
    author varchar(255),
    lang varchar(255),
    genre varchar(255),
    publisher varchar(255),
    pubyear INT,
    isbn BIGINT,
    pages INT,
    PRIMARY KEY (bookid)
);

