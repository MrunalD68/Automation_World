#Convert String to INt

number_str = "123"


number = int(number_str)
#num = int("123abc")  # ❌ ValueError: invalid literal for int()

#Convert with base (e.g., binary)

binary_str = "1010"
result = int(binary_str,2)
print("Binary to Int:",result)

print("Converted Integer:",number)