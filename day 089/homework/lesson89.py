def high(sentence):
    words = sentence.split()
    highest_score = 0
    highest_word = ""

    for word in words:
        score = sum(ord(char) - 96 for char in word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


import math

def century(year):
    return math.ceil(year / 100)
