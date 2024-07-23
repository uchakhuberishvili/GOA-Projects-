def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    elif numbers ==0:
        return 0
    elif numbers == []:
        return 0
print(find_average([20,30]))


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
print(bool_to_word(10.5))

def solution(text, ending):
    if ending in text:
        return True
    elif ending not in text:
        return False
print(solution("brocode","code"))