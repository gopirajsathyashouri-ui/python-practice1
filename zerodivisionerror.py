def calculate_average_price(total_amount, quantity):
    try:
        average = total_amount / quantity
        return average
    except ZeroDivisionError:
        return "Error: Quantity cannot be zero."
result = calculate_average_price(2000, 0)
print(result)


    