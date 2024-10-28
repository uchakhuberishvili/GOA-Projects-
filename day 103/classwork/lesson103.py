

def generate_primes(n):

    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes



def is_happy(n):
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))
    
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares(n)
    return True

