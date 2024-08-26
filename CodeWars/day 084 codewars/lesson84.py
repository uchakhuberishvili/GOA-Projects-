# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    if number < 0:
        return 0
    total_sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    
    return total_sum

# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        if len(pair) < 2:
            pair += '_'
        pairs.append(pair)
    return pairs
