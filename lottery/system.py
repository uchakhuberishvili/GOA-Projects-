import random
import time

def create_teams(players):
    random.shuffle(players)
    teams = []
    for i in range(0, len(players), 2):
        team = players[i:i+2]
        if len(team) == 2:
            teams.append(team)
    return teams

players = [
    "ucha khuberishvili", "nikoloz qimeridze", "ilia dzindzibadze", "cotne gujabidze", 
    "shalva shubitidze", "zuka abashidze", "giga khutsishvili", "berdia beqauri",
    "sandro zabakhidze", "vano motiashvili", "guram vakhtangashvili", "daniel abramiani", 
    "nika edisherashvili", "giorgi xmaladze", "data fofxadze", "alex pitava", 
    "gobron witlauri", "erekle kilasonia", "andria alavidze", "nika nutsubidze", 
    "guram papunashvili", "nikoloz whitadze", "giorgi varadashvili", "nika kvaratshelia", 
    "george gvritishvili", "saba isakadze", "ani razmadze", "luka lortqifanidze", 
    "davit narimanidze", "giorgi shavadze"
]

games = ["chess", "codewars", "kahoot"]

teams = create_teams(players)
for i, team in enumerate(teams, start=1):
    print(f"Team {i}: {team[0]} and {team[1]}")
    for seconds in range(5, 0, -1):
        print(f"Starting next team in {seconds} seconds...", end="\r")
        time.sleep(1)
    print("\n")

print("\nFinal list of all teams and games:")
for i, team in enumerate(teams, start=1):
    game = random.choice(games)
    print(f"Team {i}: {team[0]} and {team[1]} are playing {game}")
