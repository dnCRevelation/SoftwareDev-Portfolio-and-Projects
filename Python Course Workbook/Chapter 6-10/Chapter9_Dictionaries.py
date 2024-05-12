filename = input('Enter filename: ')
fhandle = open(filename)

dictionary = {}
# Empty Dictionary
for line in fhandle:
    line = line.rstrip()
    # Removing whitespace and reading lines in file line by line

    words = line.split()
    # Splitting words from lines into individual strings 

    for word in words:
        ovalue = 0
        if word in dictionary: ovalue = dictionary[word]  # Placing words from the file into empty dictionary
        dictionary[word] = ovalue + 1  # Counting the duplicate words from the file and assigning that value to the words in the dictionary e.g. {word:1}

lst = []
for w in dictionary.items():
    lst.append(w)
    lst.sort()

print(dictionary, '\n', '\n', lst)         