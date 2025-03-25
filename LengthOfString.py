#How do you find the length of a string without using len() or built-in functions?

def string_length(s):
    count=0
    for _ in s:
        count+=1
    return count

text = input("Enter a String:")
length= string_length(text)
print(f"The length of the string is: {length}")

# Explanation:

# The program defines a function string_length() that takes a string as input.
#
# It uses a for loop to iterate over each character in the string and increments the count by 1.
#
# Finally, it returns the total count.