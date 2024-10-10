import math

def nearest_sq(n):
    root = int(math.sqrt(n))
    square_below = root ** 2
    square_above = (root + 1) ** 2
    
    if n == square_below:
        return n
    
    if (n - square_below) <= (square_above - n):
        return square_below
    else:
        return square_above
    
def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result
