#How do you split a string by a delimiter (e.g., comma, space)? in python

# Split by Comma

text = "Mrunal,MAdhav,MAnaswi"
comma = text.split(",")
print(f"Split by comma characters or strings: {comma}")

#Split by Space

sentence = "Hello,Good Morning to Automation World"
space = sentence.split(" ")
print(f"Split by Space : {space}")

#Split by Multiple Spaces or Tabs

text = "Python    is\tawesome"
words = text.split()
print(f"Split by Multiple Space or Tabs:{words}")

#Split by Newline

data = "line1\nline2\nline3"
lines = data.split("\n")
print(f"Split by New Line : {lines}")

#Limiting the Number of Splits

num= "a,b,c,d,e"
limit = num.split(",",4)
print(f"Limiting the Number of Splits : {limit}")

#Using re.split() for More Complex Delimiters

import re
text1 = "apple;orange|banana,grape"
result1 = re.split(r'[;|,]',text1)
print(result1)