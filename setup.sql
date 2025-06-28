CREATE DATABASE email_signal_processing;

USE email_signal_processing;

CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    timestamp DATETIME NOT NULL,
    links TEXT
);

CREATE TABLE signals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email_id INT NOT NULL,
    domain_reputation VARCHAR(255),
    url_entropy FLOAT,
    sender_spoof_check BOOLEAN,
    FOREIGN KEY (email_id) REFERENCES emails(id)
);