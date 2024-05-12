filename = input('Enter file name: ')
fhandle = open(filename)

count = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        email = words[1]
        print(email)
print('There were', count, 'lines in the file with From as the first word.')
    
        
        

