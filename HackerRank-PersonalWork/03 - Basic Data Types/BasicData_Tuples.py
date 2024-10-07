if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    for i in range(len(t)):
        t1 = hash(t)
    print(sum(t1))
