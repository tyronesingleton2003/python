x = 20 # Defining a global variable
def my_function(): # Defining a function
  x = 30 # Defining a local variable
  print(x, end=' ') # Expected Output: 30, ending with a space

my_function() # Calling the function
print(x, end=' ') # Expected Output: 20, ending with a space