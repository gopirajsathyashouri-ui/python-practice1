def is_palindrome(text):
    text = text.lower().replace(" ", "")
    text1 = text[: : -1]
    if text == text1:
        return True
    else :
        return False

text = "A man a plan a canal Panama"
print(is_palindrome(text))

