def square_up(n):
    result = []
    for i in range(1, n + 1):
        result.extend([0] * (n - i))
        result.extend(range(i, 0, -1))
    return result

def membership_category(members):
    categories = []
    for member in members:
        age, handicap = member
        if age >= 55 and handicap > 7:
            categories.append('Senior')
        else:
            categories.append('Open')
    return categories

input_data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = membership_category(input_data)
print(output)