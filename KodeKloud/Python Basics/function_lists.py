def multiply_values(list): # Define a function 'multiply_values' that takes one parameter 'list'
    multiplied_values = [] # initialize an empty list to store the multiplied values 

    for item in list: 
        multiplied_values.append(item * 2) # multiply each item by 2 and append to the new list

    return multiplied_values # return the new list with multiplied values

print(multiply_values([1, 2, 3])) # call the function with a sample list and print the result