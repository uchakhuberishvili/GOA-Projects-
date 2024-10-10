def contamination(text, char):
    text_after = ""
    for i in text:
        text_after += char
    return text_after

print(contamination("heelo world","g"))


def two_decimal_places(n):
    return (round(n, 2))

def points(games):
    total_points = 0
    
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points

