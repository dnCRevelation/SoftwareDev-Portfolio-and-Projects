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