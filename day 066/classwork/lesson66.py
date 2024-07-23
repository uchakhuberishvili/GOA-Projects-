def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    
    result = []
    
    for i in range(0, len(s), 2):
        result.append(s[i] + s[i + 1])
    
    return result

def solution(s):
    if len(s) % 2 == 1:
        s = s + "_"
    res = ""
    count = 0
    for char in s:
        res += char
        count += 1
        if count % 2 == 0:
            res += "|"
    return (res.split("|"))[:-1]


def alphabet_position(text):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in text.lower():
        if char.isalpha():   
            index = alphabet.index(char) + 1
            result.append(str(index))
    
    return " ".join(result)

