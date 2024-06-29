def invert(lst):
    result = []
    
    for i in lst:
        if i != 0:
            result.append(-i)
        else:
            result.append(0)

        return result


def smash(words):
    result = " ".join(words)
    return result
print(smash("hello ucha is best"))

def between(a,b):
    result = []
    for i in range(a,b):
        result.append(i)
    result.append(b)
    return result

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'
    

def collatz(n):
    result = [n]
    while n != 1 :
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result