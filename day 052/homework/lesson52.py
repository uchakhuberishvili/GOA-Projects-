def getCount(s):
    return sum(c in 'aeiou' for c in s)


def xo(s):
    s_lower = s.lower()
    count_x = s_lower.count("x")
    count_o = s_lower.count("o")
    return count_x == count_o

print(xo("xxoo"))


def maps(a):
    doubled = []
    for i in a:
        doubled.append(i * 2)
    return doubled

print(maps([23,45,12,54]))


def rps(p1, p2):
    if p1 == "rock" and p2 =="scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 =="paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 =="rock":
        return "Player 1 won!"
    elif p1 == "paper" and p2 =="scissors":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 =="paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 =="rock":
        return "Draw!"
    elif p1 == "scissors" and p2 =="scissors":
        return "Draw!"
    elif p1 == "paper" and p2 =="paper":
        return "Draw!"
print(rps("scissors","paper"))



def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo!"
    else:
        return name + " does not play banjo!"
print(are_you_playing_banjo("richard"))


