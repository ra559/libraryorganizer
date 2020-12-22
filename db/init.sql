CREATE DATABASE liborg;
USE liborg;


CREATE TABLE users(
    user_email varchar(255) NOT NULL,
    user_passwd VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_email)
);

CREATE TABLE books(
    isbn varchar (255) NOT NULL,
    title varchar(255) NOT NULL,
    author varchar(255),
    lang varchar(255),
    genre varchar(255),
    publisher varchar(255),
    PRIMARY KEY (isbn)
);

INSERT INTO users VALUES ('123@HAHA.COM','123');
INSERT INTO books VALUES ('978-0-385-12168-2','The Stand','Stephen King','English','Post Apocaliptic','Doubleday');
INSERT INTO books VALUES ('978-1948836531','Indistractable','Nir Eyal','English','Self help','BenBella Books');

