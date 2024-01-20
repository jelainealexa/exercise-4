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

# Display result
print("Original word: ", original_string_1)
print("Original word: ", original_string_2)

# Outputs
print(remove_chars("Polytechnic", 4))
print(remove_chars("University", 3))