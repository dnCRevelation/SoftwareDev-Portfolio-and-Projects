# .intersection() or & - Returns a set of elements that are in both sets
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.intersection(b)))