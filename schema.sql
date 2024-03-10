CREATE TABLE users(
id int PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20) not null,
email VARCHAR(50) not null,
password VARCHAR(255) not null,
icon varchar(255)
);

CREATE TABLE orders(
id int PRIMARY KEY AUTO_INCREMENT,
user_ID INT not null,
MessageText VARCHAR(255) not null,
is_active TINYINT(1) NOT NULL,
FOREIGN KEY (user_ID) REFERENCES users(id)
);