len = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = list(input().strip().split())
    s2 = set(int(x) for x in input().strip().split())
    if command[0] == 'intersection_update':
        A.intersection_update(s2)
    elif command[0] == 'update':
        A.update(s2)
    elif command[0] == 'symmetric_difference update':
        A.symmetric_difference_update(s2)
    elif command[0] == 'difference_update':
        A.difference_update(s2)

print(sum(A))