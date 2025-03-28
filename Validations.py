#How do you check if a string contains only digits, alphabets, or special characters? in python


#Check for Digits

text = "12345"
print(f"Check For Digits : {text.isdigit()}")

#Check for Alphabets

text1 = "Python"
print(f"Check For Digits :{text1.isalpha()}")

# Check for Alphanumeric (Digits + Alphabets)

text2 = "Python123"
print(f"Check for Alphanumeric Digits : {text2.isalnum()}")

#Check for Special Characters

import string
text3 = "@#$%"
special = all(char in string.punctuation for char in text3)
print(f"Check for Special Characters : {special}")

#Combined Check


def check_string_type(s):
    if s.isdigit():
        return "Digits"
    elif s.isalpha():
        return "Alphabets"
    elif s.isalnum():
        return "Alphanumeric"
    elif all(char in string.punctuation for char in s):
        return "Special Characters"
    else:
        return "Mixed Content"

print(check_string_type("123"))
print(check_string_type("Hello"))
print(check_string_type("Hello123"))
print(check_string_type("!@#$%"))
print(check_string_type("Hello@123"))
