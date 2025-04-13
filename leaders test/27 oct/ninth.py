
# 9) Prime time (4 ქულა)

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i ==0:
            return False
    return True

def prime_max(maxb):
    primes = []
    for num in range(2,maxb + 1):
        if prime(num):
            primes.append(num)
    return primes
print(prime_max(2000))