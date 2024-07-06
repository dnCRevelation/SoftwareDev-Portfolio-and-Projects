from itertools import groupby

a = input()
grouped = groupby(a)
result = []
for char, group in grouped:
    count = len(list(group))
    result.append(f"({count},{char})")

result_str = ' '.join(result)
print(result_str)

