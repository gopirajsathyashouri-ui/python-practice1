#stringmethods.py
string = "alma better"
print(string.upper())
print(string.lower())
print(string.title())
print(string.replace("better", "better than"))

string1 = string.split(" ")
print(string1)

string2 = " ".join(string1)
print(string2)
