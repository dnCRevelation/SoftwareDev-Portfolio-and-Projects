# .union() or | - Returns a set of all elements in two sets
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.union(b)))