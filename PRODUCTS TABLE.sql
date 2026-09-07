CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    discount DECIMAL(10, 2)
);

INSERT INTO product (product_id, product_name, price, discount)
VALUES
(1, 'Laptop', 55999.75, 2500.50),
(2, 'Mouse', 699.40, 50.00),
(3, 'Keyboard', 1299.90, 150.25),
(4, 'Monitor', 10500.60, 800.75);