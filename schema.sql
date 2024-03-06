CREATE TABLE users(
id int PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20) not null,
email VARCHAR(50) not null,
password VARCHAR(255) not null
);

CREATE TABLE orders(
id int PRIMARY KEY AUTO_INCREMENT,
user_ID INT not null,
MessageText VARCHAR(255) not null,
FOREIGN KEY (user_ID) REFERENCES users(id)
);