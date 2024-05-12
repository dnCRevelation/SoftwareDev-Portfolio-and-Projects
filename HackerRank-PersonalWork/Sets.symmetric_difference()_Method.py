# .symmetric_difference() or ^ - Returns a set of elements in either set but not in both
a = int(input())
A = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(y) for y in input().strip().split()])

print(len(A.symmetric_difference(B)))
