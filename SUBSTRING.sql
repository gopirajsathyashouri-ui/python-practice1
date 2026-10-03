SELECT email,
SUBSTRING(email FROM 1 FOR 5) AS email_prefix
FROM customer;