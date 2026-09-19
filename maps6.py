prices = [100, 250, 75, 300]

def apply_discount(price):
    discounted_price = price - (price * 0.1)
    return discounted_price

result = map(apply_discount, prices)
print(list(result))