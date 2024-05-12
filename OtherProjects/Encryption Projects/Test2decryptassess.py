def decode(message_file):
    """
    Function to decode an encoded message from a .txt file.

    Parameters:
    - message_file: str
        The path to the .txt file containing the encoded message.

    Returns:
    - str:
        The decoded version of the message as a string.

    Raises:
    - FileNotFoundError:
        If the specified file does not exist.
    """

    try:
        # Opening the file in read mode
        with open(message_file, 'r') as file:
            # Reading the contents of the file
            content = file.read()

            # Splitting the content into words
            words = content.split()

            # Mapping the words to their associated numbers
            word_map = {
                '1': 'I',
                '3': 'love',
                '6': 'computers'
            }

            # Decoding the message by replacing the numbers with their associated words
            decoded_message = ' '.join([word_map[word] for word in words])

            return decoded_message

    except FileNotFoundError:
        raise FileNotFoundError("The specified file does not exist.")
    


def do_triangle(max_number):
    """Print numbers and return end of line numbers."""
    count = 0  # Initialise value
    line_length = 0  # Initialise line number
    triangle_numbers = []  # Initialise list of triangular numbers
    while True:
        line_length += 1  # Next line
        for _ in range(line_length):
            count += 1  # Next number
            print(count, end=' ')
        print()  # Start new line
        # Add the current count (end of line) to the list.
        triangle_numbers.append(count)
        # Stop at end of line when count >= max_number.
        if count >= max_number:
            return triangle_numbers


# Map words to numbers with a dictionary
word_map = {2: 'orange', 6: 'cake', 4: 'thread', 1: 'I', 5: 'piano', 3: 'like'}

# Look up each triangular number in word_map
for i in do_triangle(len(word_map)):
    # and print it (with a space at the end).
    print(word_map.get(i), end=' ')

# Example usage:
message_file = 'C:/Users/JPWil/OneDrive/Desktop/message_file.txt'
decoded_message = decode(message_file)
print(decoded_message)

def decode(text_file):
with open('text_file.txt', 'r') as file:
    lines = file.readlines()

message_dict = {}

for line in lines:
    number, word = line.split()
    message_dict[int(number)] = word

pyramid_numbers = []

i = 1
while i <= len(message_dict):
    pyramid_numbers.append(i)
    i += 1
    print(pyramid_numbers)

message = ''.join([message_dict[number] for number in pyramid_numbers])

return message
print(decode('text_file'))