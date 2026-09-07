SELECT 
    product_name,
    price,
    ROUND(price, 0) AS rounded_price
FROM product;