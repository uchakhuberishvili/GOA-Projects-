def solution2(s):
    if len(s) % 2 != 0:
        s += '_'
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    return pairs
print(solution2("hello!"))
