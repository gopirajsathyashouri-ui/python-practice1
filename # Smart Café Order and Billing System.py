# Smart Café Order and Billing System

customer_name = "Aarav"
customer_age = 22 

coffee_price  = 180
sandwich_price = 150.0
coffee_quantity = 2
sandwich_quantity = 1

is_member = True
coupon_code = "BREW10"

ordered_items = ["Coffee", "Sandwich", "Coffee"]
available_items = ("Coffee", "Tea", "Sandwich", "Muffin")

selected_addons = {"Extra Sugar", "Whipped Cream"}
free_addons = {"Extra Sugar", "Chocolate Syrup"}

customer_details = {
    "name": "Aarav",
    "city": "Bengaluru",
    "membership": "Gold"
}

delivery_partner = None
coffee_total = coffee_price * coffee_quantity 
sandwich_total = sandwich_price * sandwich_quantity
sub_total = coffee_total + sandwich_total
print(coffee_total)
print(sandwich_total)
discount = (sub_total * 10) / 100
bill_after_discount = sub_total - discount
print(discount)
print(bill_after_discount)
gst_amount = (bill_after_discount * 5) / 100
final_bill = bill_after_discount + gst_amount
print(gst_amount)
print(final_bill)
has_free_delivery = final_bill >= 500 or is_member
print("Free Delivery:", has_free_delivery) 

