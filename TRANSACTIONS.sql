DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10, 2),
    transaction_date DATE
);

INSERT INTO transactions (customer_id, amount, transaction_date)
VALUES
    (101, 50.00, '2024-04-01'),
    (101, 150.00, '2024-04-03'),
    (102, 75.00, '2024-04-01'),
    (102, 120.00, '2024-04-03'),
    (103, 100.00, '2024-04-02'),
    (103, 90.00, '2024-04-04'),
    (103, 100.00, '2024-04-05');