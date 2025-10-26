def get_even_func(numbers): # Define a function that takes a list of numbers as input
    even_numbers = [ num for num in numbers if not num % 2 ] # Use list comprehension to filter even numbers
    return even_numbers # Return the list of even numbers

get_even_func([1, 2, 3, 4, 5, 6]) # Call the function with a sample list of numbers
# Expected output: [2, 4, 6]