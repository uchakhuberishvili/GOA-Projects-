class Hero:
    def __init__(self, name='Hero'):
        self.name = name              
        self.position = '00'          
        self.health = 100             
        self.damage = 5              
        self.experience = 0




def points(games):
    total_points = 0
    
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points


def count(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1

    return result
    