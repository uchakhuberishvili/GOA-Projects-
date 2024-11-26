def is_isogram(string):
    string = string.lower().replace(" ", "")
    return len(string) == len(set(string))

print(is_isogram("Dermatoglyphics"))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

def divisors_sum(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(divisors)