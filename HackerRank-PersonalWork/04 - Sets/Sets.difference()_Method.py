# .difference() or - - Returns a set of elements in the first set that are not in the second set
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.difference(b)))