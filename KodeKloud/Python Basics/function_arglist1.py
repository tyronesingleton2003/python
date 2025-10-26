def sum(*args): # function that takes variable number of arguments
    for arg in args: # iterate through each argument
        result += arg # add each argument to result 
    return result # return the final sum

print(sum(2,3,1)) # Output: 2   