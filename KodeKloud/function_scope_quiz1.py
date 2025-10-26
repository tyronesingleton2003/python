def my_function(): # defining an outer function
    x = 20  # Local variable in the outer function
    def my_inner_function(): # defining an inner function
        print(x)  # Accessing the outer function's variable x
    my_inner_function()  # Calling the inner function
my_function()  # Output: 20 Function demonstrating variable scope