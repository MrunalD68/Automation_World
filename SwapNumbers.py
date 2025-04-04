#Write a python program to swap two numbers without using a third variable.

a=5
b=10

print("Before Swap:")
print("a=",a)
print("b=", b)

# Swapping without using a third variable

a= a+b # a becomes 15
b= a-b # b becomes 5 (original value of a)
a= a-b # a becomes 10 (original value of b)

print("After Swap:")
print("a= ",a)
print("b =",b)