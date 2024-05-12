filename = input('Enter filename: ')
fhandle = open(filename)

ndict = {}
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        ndict[line[1]] = ndict.get(line[1], 0) + 1

sender = None
svalue = 0
for key, value in ndict.items():
    if sender is None or value > svalue:
        sender = key
        svalue = value
        
        
print(sender, svalue)