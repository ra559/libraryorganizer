CREATE DATABASE liborg;
USE liborg;

CREATE TABLE users(
    user_email varchar(255) NOT NULL,
    user_passwd VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_email)
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

INSERT INTO USERS VALUES ('123@HAHA.COM','123');
