import re
def val_regex(s):
    try: 
        re.compile(s)
        return "True"
    
    except Exception:
        return "False"
    
T = int(input())

for i in range(T):
    s = input()
    res = val_regex(s)
    print(res)
    


