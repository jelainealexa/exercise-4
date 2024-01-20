# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Def function
def remove_chars(string, n):
    # Check if n is less than the length of the string
    if n < len(string):
        # Use string slicing
        result = string[n:]
        return result
    else:
        print("Error! Must be less than the length of the word.")
        return None

# Define original string
original_string_1 = "Polytechnic"
original_string_2 = "University"

# Display result of first string
print("Original word: ", original_string_1)

# Output: technic
print(remove_chars("Polytechnic", 4))

# Display result of second string
print("Original word: ", original_string_2)

# Output: versity
print(remove_chars("University", 3))