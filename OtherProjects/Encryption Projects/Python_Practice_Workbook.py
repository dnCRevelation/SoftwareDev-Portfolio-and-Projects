import random

print("Welcome to Team Allocator\n")

players = ["Sarah", "Jeff", "James", "Ny", "Kim", "Quantino", "Travette", "John", "Shaquan", "Agnes"]

while True:

    random.shuffle(players)
    response = input("Is this a team or individual sport? \
                     \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//2]
        print("Team 1 Captain: " + random.choice(team1))
        print("\nTeam 1: \n")
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]
        print("\nTeam 2 Captain: " + random.choice(team2))
        print("\nTeam 2: \n")
        for player in team2:
            print(player)
    else:
        for i in range(0,10,2):
            print(players[i] + " vs " + players[i+1])
            start = random.randrange(i, i+2)
    
    response = input("Pick Teams Again? (y/n):  ")
    if response == "n":
        break











