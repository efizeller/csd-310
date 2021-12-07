DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('3425 52nd street, Miami Florida, 12345');



INSERT INTO book(book_name, author, details)
    VALUES('Intro to NoSQL', 'Bill Doe', 'NoSQL Programming and Data Structures');

INSERT INTO book(book_name, author, details)
    VALUES('Intro To SQL', 'Bill Doe', 'SQL For Begginers');

INSERT INTO book(book_name, author, details)
    VALUES('Intro To SQL 2', 'Bill Doe', 'SQL For Begginers Part 2');

INSERT INTO book(book_name, author, details)
    VALUES('Access Control', 'Bob Reynold', 'Intro To Access Control');

INSERT INTO book(book_name, author, details)
    VALUES('Access Control 2', 'Bob Reynolds', 'Intro To Access Control Part 2');

INSERT INTO book(book_name, author, details)
    VALUES("Access Control 3", 'Bob Reynolds', 'Intro To Access Control Part 2');

INSERT INTO book(book_name, author, details)
    VALUES('Intro To Forensics', 'Ryan Joel', 'Forensics For begginers');

INSERT INTO book(book_name, author, details)
    VALUES('Intro To Forensics 2', 'Ryan Joel', 'Forensics For Begginers Part 2');

INSERT INTO book(book_name, author, details)
    VALUES('Intro To Forensics 3', 'Ryan Joel', 'Forensics For Begginers Part 3');




INSERT INTO user(first_name, last_name) 
    VALUES('John', 'Kean');

INSERT INTO user(first_name, last_name)
    VALUES('Robert', 'Doe');

INSERT INTO user(first_name, last_name)
    VALUES('Paul', 'King');




INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'), 
        (SELECT book_id FROM book WHERE book_name = 'Access Control')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Robert'),
        (SELECT book_id FROM book WHERE book_name = 'Access Control 3')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Paul'),
        (SELECT book_id FROM book WHERE book_name = 'Intro To SQL 2')
    );
