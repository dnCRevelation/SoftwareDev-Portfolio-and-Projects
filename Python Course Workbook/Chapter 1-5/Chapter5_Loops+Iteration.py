###########################
#### LOOPS + ITERATION ####
###########################

num = 0
tot = 0.0
while True :
    sval = input('Enter a Number: ')
    if sval == 'done':
        break
    # Error code upon typing words but not cancelling the loop
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue  # Continuing the loop if words are typed
    fval = float(sval)
   # Calculations
    num = num + 1
    tot = tot + fval

# Summing the avg of all numbers input by the user
print(tot, num, tot/num) 