fname = input('Enter file name: ')

try:
    handle = open(fname)
except:
    print('File does not exist, please try again.')
    quit()

num = 0
sum = 0

for line in handle:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        list = float(line[19:])
        num = num + 1
        sum = sum + list

total = sum / num
print('Average spam confidence:', total)       

        
        

