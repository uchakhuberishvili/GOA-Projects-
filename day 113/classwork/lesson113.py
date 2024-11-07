def descending_order(n):
    sorted_digits = ''.join(sorted(str(n), reverse=True))
    return int(sorted_digits)


def get_sum(a, b):
    if a == b:
        return a
    return sum(range(min(a, b), max(a, b) + 1))


def same_case(char1, char2):
    if not (char1.isalpha() and char2.isalpha()):
        return -1
    elif (char1.islower() and char2.islower()) or (char1.isupper() and char2.isupper()):
        return 1
    else:
        return 0