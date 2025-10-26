age = int(input("What is your age? ")) # Setting the age variable, as an integer, requesting user input,

if age >= 18: # evaluating if age variable is less than 18
    if age == 18: # creating a nested loop
        print("You are exactly 18 years old.") 
    else: # meeting condition if age variable is more than 18
      print("You are " + str(age) + ". You are older than 18 years old.") 
else: # Meeting condition if age variable is younger than 18
    print("You are younger than 18.")
