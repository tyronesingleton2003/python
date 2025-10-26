ages = [56, 72, 24, 46] # creating an ages variable of numbers
total = 0  # assigning the total variable a value of zero
for age in ages: #looping through the ages list
    total += age # looping through the ages list, adding each value to the 'total' variable
    print(total) # prints the current value of the total within the loop
average = total/len(ages) # setting an average variable by dividing the total of all of the ages and the length of the ages variable
print(average) # prints the average variable
