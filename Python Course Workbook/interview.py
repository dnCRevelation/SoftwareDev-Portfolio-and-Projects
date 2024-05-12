n = int(input()); s = set([int(x) for x in input().strip().split()]); N = int(input())
print(n, s)
for i in range(N):
    command = list(input().strip().split())
    if command[0] == 'pop':
        s.pop()
        print(s)
    elif command[0] == 'remove':
        s.remove(int(command[1]))
        print(s)
    elif command[0] == 'discard':
        s.discard(int(command[1]))
        print(s)

print(sum(s))
### Sets ###

# .intersection() or & - Returns a set of common elements in two sets
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.intersection(b)))

# .union() or | - Returns a set of all elements in two sets
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.union(b)))

# .difference() or - - Returns a set of elements in the first set that are not in the second set
N = int(input())
n = set([int(x) for x in input().strip().split()])
B = int(input())
b = set([int(x) for x in input().strip().split()])
print(len(n.difference(b)))

# .symmetric_difference() or ^ - Returns a set of elements in either set but not in both
a = int(input())
A = set([int(x) for x in input().strip().split()])
b = int(input())
B = set([int(y) for y in input().strip().split()])

print(len(A.symmetric_difference(B)))

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


