def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_cubes(numbers):

    return sum(n**3 for n in numbers)

def find_smallest_prime(n):
    if n <= 1:
        return None
    for num in range(n, 0, -1):
        if is_prime(num):
            return num
        return None
