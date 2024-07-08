def solution(s):
    split_list = []

    if len(s) % 2 != 0:
        s += "_"
    
    for i in range(0,len(s), 2):
        second = s[i + 1]
        split_list.append(s[i] + second)
    
    return split_list
print(solution("hello"))