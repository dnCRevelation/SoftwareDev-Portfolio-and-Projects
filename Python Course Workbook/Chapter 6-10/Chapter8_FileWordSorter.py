filename = input('Enter file name: ')
fhandle = open(filename)
lst = list()
for line in fhandle:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst)

        
        

