#Write a Pyhton program to find duplicate elements in an array.

def find_duplicates(arr):
    seen = set() # Set to store unique elements
    duplicates = set()   # Set to store duplicate elements

    for num in arr:
        if num in seen:
            duplicates.add(num) # If already seen, add to duplicates set
        else:
            seen.add(num) # Otherwise, add to seen set


    return list(duplicates) # Convert set to list for output


arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
print("Duplicate Elements :", find_duplicates(arr))