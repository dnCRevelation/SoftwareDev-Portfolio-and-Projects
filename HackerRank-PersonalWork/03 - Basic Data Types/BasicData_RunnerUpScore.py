n = int(input())
arr = list(map(int, input().split())) # NOTE TO SELF: IF MAP IS NOT SPLITTING PROPERLY, INPUT SPACES IN BETWEEN INTEGERS!
print(sorted(set(arr), reverse=True)[1])



