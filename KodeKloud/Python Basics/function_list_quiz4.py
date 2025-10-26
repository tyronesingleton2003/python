def double_list(numbers): # Function to double each number in the list
    return 2 * numbers # # This will cause an error because we are trying to multiply a list by an integer directly

numbers = [1, 2, 3]
print(double_list(numbers))  # Output: [2, 4, 6 ]