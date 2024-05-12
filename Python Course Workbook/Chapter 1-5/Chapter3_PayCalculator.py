hrs = input("Enter Hours: ")

try:
    float(hrs)
except:
    print("Number Error, Please enter a Numeric Value and Try Again.")
    quit()

rate = input("Enter Hourly Rate: ")

try:
    float(rate)
except:
    print("Number Error, Please enter a Numeric Value and Try Again.")
    quit()

h = float(hrs)
r = float(rate)
gross = h * r
overtime = 40 * r + (h - 40) * (r * 1.5)

if h <= 40.0:
    print(gross)
else:
    print(overtime)


