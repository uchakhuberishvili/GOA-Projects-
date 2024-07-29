def expression_matter(a, b, c):

    results = [
        a + (b + c),
        (a + b) + c,
        a * (b + c),
        (a + b) * c,
        a + (b * c),
        (a * b) + c,
        a * b * c,
        (a * b) * c
    ]
    return max(results)

def between_extremes(numbers):
    if len(numbers) < 2:
        raise ValueError("The array must contain at least two elements.")
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value - min_value


def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
