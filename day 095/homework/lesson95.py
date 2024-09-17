def is_isogram(string):
    return len(string) == len(set(string.lower()))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            return factors
        
def sum_of_multiples(limit, multiples):
    return sum(i for i in range(limit) if any(i % m == 0 for m in multiples))