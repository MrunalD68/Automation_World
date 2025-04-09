# Convert Int to String

#Method 1:Using str() function
number = 123
str_value = str(number)
print("Converted String:",str_value)
print("Data Type:",type(str_value))

#Method 2: Using f-strings (Python 3.6+)

num = 1234
result = f"{num}"
print("Converted String:",result)
print("Data Type:",type(result))

#Method 3: Using format() method

num1 = 12345
value = "{}".format(num1)
print("Converted String:", value)
print("Data Type:", type(value))
