import random

players = []
print("Welcome to Team/Player Selector!\n")
number_of_players = int(input("How many players are there? "))
for i in range(1, number_of_players + 1):
    players.append(i)


while True:

    random.shuffle(players)
    response = input("Is this a team or individual sport? \
                     \nType team or individual: ")
    if response == "team":
        team1 = players[:len(players)//2]
        print("Team 1 Captain: " + str(random.choice(team1)))
        print("\nTeam 1: \n")
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]
        print("\nTeam 2 Captain: " + str(random.choice(team2)))
        print("\nTeam 2: \n")
        for player in team2:
            print(player)
        
    else:
        for i in range(0,number_of_players,2):
            print(str(players[i]) + " vs " + str(players[i+1]))
            start = random.randrange(i, i+2)
            print(str(players[start]) + " starts first!")
    
    response = input("Pick Teams Again? (y/n):  ")
    if response == "n":
        print("Thank you for playing!")
        break











