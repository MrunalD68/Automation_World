def reverse_string(s):
    # Reverse the string manually
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Main program with validation
while True:
    original = input("Enter a string to reverse (or 'q' to quit): ").strip()

    if original.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break

    # Validation: Check if the input contains only alphabetic characters
    if not original.isalpha():
        print("Invalid input. Please enter alphabetic characters only.")
        continue

    # Display the reversed string
    reversed_result = reverse_string(original)
    print(f"Reversed string: {reversed_result}")
