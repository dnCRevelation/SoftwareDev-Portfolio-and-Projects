### Set Mutations ###

# .update() or |= - Updates the set by adding elements from another set
n = int(input())
N = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(x) for x in input().strip().split()])
N.update(B)
print(sum(N))

# .intersection_update() or &= - Updates the set by keeping only elements found in another set
n = int(input())
N = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(x) for x in input().strip().split()])
N.intersection_update(B)
print(sum(N))

# .difference_update() or -= - Updates the set by removing elements found in another set
n = int(input())
N = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(x) for x in input().strip().split()])
N.difference_update(B)
print(sum(N))

# .symmetric_difference_update() or ^= - Updates the set by removing elements found in both sets
n = int(input())
N = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(x) for x in input().strip().split()])
N.symmetric_difference_update(B)
print(sum(N))
