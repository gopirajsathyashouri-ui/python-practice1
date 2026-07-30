# Discounted Price Calculator 
def calculate_discounted_price(price, discounted_percent) :
    discounted_amount = price * discounted_percent // 100
    final_price = price- discounted_amount
    return final_price

result = calculate_discounted_price(1000, 10)
print(result)
