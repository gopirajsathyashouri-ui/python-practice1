CREATE TABLE users (
    name VARCHAR(255),
    age INT,
    city VARCHAR(255)
);
INSERT INTO users
VALUES
    ('Ravi', 24, 'New Delhi'),
    ('Kartik', 37, 'Mumbai'),
    ('Sagar', 31, 'New Delhi'),
    ('Vikram', 26, 'Mumbai');

SELECT * FROM users WHERE age > 30 AND city = 'Mumbai';