def bonus_time(salary, bonus):
    if bonus :
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
    
def count(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1

    return result
    
def get_count(sentence):
    result = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            result += 1

    return result


def sumAverage(arr):
    result = 0
    sums = 0
    for i in arr:
        sums += i
        result += sums / len(arr)
    return result


def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)