#How do you remove white spaces from the beginning and end of a string?


#.strip() → Removes leading and trailing white spaces.
text = "     Hello,Good Morning      "
result = text.strip()
print(f"Strip : {result}")

#.lstrip() → Removes only leading (left) white spaces.

text1= "    Hello Good Morning         "
result1 = text1.lstrip()
print(f"LStrip : {result1}")

#.rstrip() → Removes only trailing (right) white spaces.

text2 = "  Hello, Good MOnring       "
result2 = text2.rstrip()
print(f"RStrip : {result2}")