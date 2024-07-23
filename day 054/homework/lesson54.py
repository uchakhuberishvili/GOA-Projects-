def smash(words):
    wordss = ""
    for i in words:
        wordss += i + " "
    return wordss[:-1]
print(smash(['hello', 'world', 'this', 'is', 'great']))
    

def square_sum(numbers):
    numbs = []
    Sum = 0
    for i in numbers:
        s = i * i
        numbs.append(s)
    for i in numbs:
        Sum += i
    return Sum
print(square_sum([2,5,3]))



def greet(name, owner):
    if name == owner:
        return("Hello boss")
    else:
        return("Hello guest")
print(greet("nika","nika"))


def sum_array(a):
    Sum = 0
    for i in a:
        Sum += i
    return Sum
print(sum_array([-11,22,30]))    
