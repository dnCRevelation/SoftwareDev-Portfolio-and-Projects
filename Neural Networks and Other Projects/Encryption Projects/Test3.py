def decode(message_file):
    with open(message_file, 'r') as f:
        lines = f.readlines()

    # Split each line into a list of words
    words = [line.strip().split(' ') for line in lines]
    
    # Flatten the list of words and remove empty strings
    words = [word for sublist in words for word in sublist if word]

    numbers = sorted([int(word) for word in words if word.isdigit()])
    
    decoded_message = ""
    for num in numbers:
        word_index = num - 1
        word = words[word_index]
        decoded_message += word + " "

    return decoded_message.strip()

message_file = "C:/message_file.txt"
result = decode(message_file)
print("Decoded message:", result)