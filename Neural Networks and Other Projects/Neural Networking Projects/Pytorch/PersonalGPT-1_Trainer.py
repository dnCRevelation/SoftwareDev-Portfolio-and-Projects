# Open and Read the File
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of Characters In Dataset', len(text))

# Characters in Set
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

# Character Mapping
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]   # Take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # Take a list of integers, output a string

print(encode('Hello There'))
print(decode(encode('Hello There')))

# Importing Pytorch and registering the dataset
import torch
data = torch.tensor(encode(text), dtype=torch.long)
print(data.shape, data.dtype)
print(data[:1000]) # First 1000 Characters as it is viewed by the GPT

# Splitting the data into training, and validation sets
n = int(0.9*len(data)) # First 90% is used for training, all the rest will be for validation
train_data = data[:n]
val_data = data[n:]