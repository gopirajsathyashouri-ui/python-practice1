print("====Unit Converter====")
print("1.Celcius to Fahrenheit")
print("2.Fahrenheit to Celcius")
print("3.Kilometres to Mileds")
print("4.Miles to Kilometres")

choice = input("Enter your choice(1-4): ")
if choice == "1":
    c = float(input("Enter temp in Celcius: "))
    result = c * 9/5 + 32
    print(c, "°C =", round(result, 2), "°F")
elif choice == "2":
    f = float(input("Enter temp in Fahrenheit: "))
    result = (f - 32) * 5/9
    print(f, "°F =", round(result, 2), "°C")
elif choice == "3":
    km = float(input("Enter distance in kilometers:"))
    result = km * 0.621371
    print(km, "km =", round(result, 2), "miles")
elif choice == "4":
    miles = float(input("Enter distance in miles: "))
    result = miles / 0.621371
    print(miles, "miles =", round(result, 2), "km")
else:
    print("Invalid choice. Please enter a number from 1 t0 4")
    