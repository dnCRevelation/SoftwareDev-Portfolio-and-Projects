from itertools import combinations

n, s, k = int(input()), input().split(), int(input())

combines = list(combinations(s, k))
print(len([x for x in combines if 'a' in x]) / len(combines))
