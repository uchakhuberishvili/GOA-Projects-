def add(*args):
    sum = 0
    for i in args:
        sum += i
        return sum
print(add(421))

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
        return sum
print(add(176))