

CREATE DATABASE heartdb;
USE heartdb;

CREATE TABLE `user` (
    `name` VARCHAR(100),
    `email` VARCHAR(100) PRIMARY KEY,
    `password` VARCHAR(16)
);

INSERT INTO `user` (`name`, `email`, `password`) VALUES
    ('john', 'john@gmail.com', '123456');

CREATE TABLE feedback (
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    message TEXT
);




