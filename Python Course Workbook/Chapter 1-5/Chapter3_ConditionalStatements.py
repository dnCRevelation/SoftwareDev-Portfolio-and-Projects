score = input("Enter Score: ")

try:
    grade = float(score)
except:
    print("Error, only enter numeric values within the range of 0.0 and 1.0. Please try again.")    



if grade > 1.0:
    print("Error, only enter numeric values within the range of 0.0 and 1.0. Please try again.")
    quit()    
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")

    
    


