def captain_seeker(k, rooms):
    rooms.sort()
    for i in range(0, len(rooms), k):
        if i == len(rooms) - 1:
            return rooms[i]
        elif rooms[i] != rooms[i + 1]:
            return rooms[i]
    return -1

def main():
    k = int(input())
    rooms = list(map(int, input().split()))
    print(captain_seeker(k, rooms))

if __name__ == "__main__":
    main()
