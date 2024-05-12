def computepay(h, r):
    
    if h == hrs:
        h = float(hrs)
    
    if r == rate:
         r = float(rate)
    
    gross = h * r
    overtime = 40 * r + (h - 40) * (r * 1.5)
    
    if h <= 40.0:
            return gross
    else:
        return overtime


    

hrs = input("Enter Hours:")
rate = input("Enter Rate of Pay:")
pay = computepay(hrs, rate)
print("Pay", pay)
