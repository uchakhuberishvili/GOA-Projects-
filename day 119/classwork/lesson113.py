import math

def nearest_sq(n):
    root = int(math.sqrt(n))
    square_below = root ** 2
    square_above = (root + 1) ** 2
    
    if n == square_below:
        return n
    
    if (n - square_below) <= (square_above - n):
        return square_below
    else:
        return square_above
    

def up_array(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    num_str = ''.join(map(str, arr))
    num = int(num_str) + 1
    result = list(map(int, str(num)))
    return [0] * (len(arr) - len(result)) + result

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