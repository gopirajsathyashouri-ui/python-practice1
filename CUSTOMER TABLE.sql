CREATE TABLE customer(
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50)
);

INSERT INTO customer(customer_id, first_name, last_name, email, city)
VALUES
(1, 'aman', 'shah', 'aman@example.com', 'Mumbai'),
(2, 'riya', 'patel', 'riya@example.com', 'Ahmedabad'),
(3, 'kabir', 'mehta', 'kabir@example.com', 'Delhi');