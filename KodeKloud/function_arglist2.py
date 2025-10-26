def my_function(arg1, *argv):  # function with one normal argument and variable-length argument
    print ("First argument:", arg1) # print the first argument
    for arg in argv: # iterate through the variable-length arguments
        print("Next argument:", arg) # print each argument

my_function('Welcome', 'to', 'Python!') # calling the function with multiple arguments