text = "X-DSPAM-Confidence:    0.8475"
a = int(text.find('0'))
b = int(len(text))
print(float(text[a:b]))