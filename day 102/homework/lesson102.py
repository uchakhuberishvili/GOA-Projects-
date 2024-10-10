def problem(value):
    if isinstance(value, str):
        return "Error"
    return value * 50 + 6

def get_volume_of_cuboid(length, width, height):
    return length * width * height

def move(current_position, roll):
    if 1 <= roll <= 6:
        return current_position + (roll * 2)

class Hero:
    def __init__(self, name='Hero'):
        self.name = name              
        self.position = '00'          
        self.health = 100             
        self.damage = 5              
        self.experience = 0

def change_me(input_coin):
    accepted = {
        '£5': 500,
        '£2': 200,
        '£1': 100,
        '50p': 50,
        '20p': 20,
        '10p': 10
    }
    
    value = accepted.get(input_coin)

    if value is None:
        return input_coin

    if value == 20:
        return '10p 10p'
    elif value == 10:
        return '10p 10p'
    
    if value == 50:
        return '20p 20p 10p'

    change_20p = value // 20
    remainder = value % 20
    change_10p = remainder // 10

    change_list = ['20p'] * change_20p + ['10p'] * change_10p

    if change_list == ['20p', '20p']:
        return '10p 10p'

    return ' '.join(change_list)
