def input_number(num1, num2): # Function with two arguments
    return int(input("Enter a number: ")) * num1 - num2 # Returns the result of the expression using the input number and the two arguments
input1 = input_number(num1 = 10, num2 = 20) # Calls the function with named arguments
print("The result is:", input1) # Prints the result