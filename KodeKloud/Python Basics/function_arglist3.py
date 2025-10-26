def my_function(*argv):  # function with variable-length argument
    for arg in argv:  # iterate through each argument
        print(arg) # print each argument

my_function('Hello', 'World!') # calling the function with multiple arguments