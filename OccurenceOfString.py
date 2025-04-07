# Write a python program to count the occurrence of each character in a string.

def count_characters(s):
        # Create an empty dictionary to store character frequencies
        char_count = {}

        for char in s:
            # if char == '':
            #     continue # Skip spaces (optional, remove this if you want to count spaces too)

            if char in char_count:
                char_count[char]+=1 # Increment count if already exists
            else:
                char_count[char]=1 # Add new character with count 1

        # Print character frequencies
        print("Character Frequence:")
        for char,count in char_count.items():
            print(f"{char}:{count}")
# Example usage
input_str = "Hello World"
count_characters(input_str)


# # Explanation
# char_count is a dictionary that maps each character to the number of times it appears.
#
# We loop through each character in the string:
#
# If the character is already in the dictionary, we increment its value.
#
# If not, we add it to the dictionary with a count of 1.
#
# At the end, we print each character and its frequency.*/