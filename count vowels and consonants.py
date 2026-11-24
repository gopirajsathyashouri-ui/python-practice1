text = input("Enter a word: ").lower()

vowel_count = 0 
constant_count = 0

for char in text:
    if char in "aeiou":
        vowel_count += 1 
    elif char.isalpha():
        constant_count += 1 

print("Vowels:", vowel_count)
print("Constants:", constant_count)
