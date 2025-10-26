def multi_func(): # Function with multiple return statements
    result = int(input()) * 5 # # First computation
    return result # First return statement

print(result) # This line will cause an error because 'result' is not defined in this scope
#print(multi_func()) # Calling the function and printing the result