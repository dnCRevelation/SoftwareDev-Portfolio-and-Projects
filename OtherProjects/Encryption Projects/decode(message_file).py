
def decode(message_file):
    # Step 1: Read the contents of the file and store them in a list
    with open(message_file, 'r') as file:
        content = file.readlines()
    
    # Step 2: Create a dictionary to map the numbers to the corresponding words
    word_map = {}
    for line in content:
        number, word = line.split()
        word_map[int(number)] = word
    
    # Step 3: Sort the numbers in ascending order and construct the pyramid of words
    sorted_numbers = sorted(word_map.keys())
    pyramid = [sorted_numbers[:i+1] for i in range(len(sorted_numbers))]
    
    # Step 4: Retrieve the words corresponding to the numbers at the end of each line of the pyramid
    message_words = [word_map[num] for num in pyramid[-1]]
    
    # Step 5: Concatenate the retrieved words to form the decoded message
    decoded_message = ' '.join(message_words)
    
    return decoded_message

message_file = input("Enter filename: ")
decoded_message = decode(message_file)
print(decoded_message)

