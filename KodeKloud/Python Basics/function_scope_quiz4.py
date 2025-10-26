def my_function(): # defining an outer function
  def my_inner_function(): # defining an inner function
    x = 20 # Local variable in the inner function
  print(x) # Trying to access the inner function's variable x
  my_inner_function() # Calling the inner function

my_function() # This will raise a NameError because x is not defined in the scope of my_function