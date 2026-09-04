#logicaloperators.py

bag1_weight = 15
bag2_weight = 5

if bag1_weight < 13 and bag2_weight < 13:
    print("Enjoy your trip!")
else:
    print("You cannot go through")

if bag1_weight < 6 or bag2_weight < 6:
    print("You can go through")
else :
    print("You cannot go through")
    