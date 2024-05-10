def digitize(n):
    nums = []
    n = str(n)
    n = n[::-1]
    
    for i in n:
        nums.append(int(i))
    
    return nums



def no_space(x):
    result = ''
    for char in x:
        if char != ' ':
            result += char
    return result


def digitize(n):
    return [int(n) for n in str(n)[::-1]]

def digitize(n):
    return list(reversed([int(i) for i in str(n)]))

