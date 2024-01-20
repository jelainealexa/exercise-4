# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Def function
def remove_chars(string, n):
    # Check if n is less than the length of the string
    if n < len(string):
        # Use string slicing
        result = string[n:]
        return result
    else:
        return None

# Define original string

# Display result

# Outputs