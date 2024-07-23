def valid_braces(string):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False
    
    return not stack

print(valid_braces("[]{}()"))

def alphabet_position(text):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in text.lower():
        if  i.isalpha():
            res = alphabet.index(i) + 1
            result.append(str(res))
    return " ".join(result)

print(alphabet_position("hello its me asd  asd"))

def solution(s):
    result = []
    if len(s) % 2 != 0:
        s += "_"
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
print(solution("abc"))


def merge_strings(first, second):
    result = ""
    result += first
    for i in second:
        if i in result:
            pass
        elif i not in result:
            result += i
    return result

def sum_no_duplicates(l):
    result = 0
    for i in l:
        if l.count(i) > 1:
            pass
        else:
            result += int(i)
    return result


