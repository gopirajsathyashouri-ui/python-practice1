SELECT
    product_name,
    price,
    CEIL(price) AS rounded_price
FROM product;