def no_prime(start, end):
    non_primes = []
    for num in range(start, end + 1):
        if num == 1:
            non_primes.append(num)
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                non_primes.append(num)
    return non_primes



print(no_prime(10, 20))
print(no_prime(1, 10))
print(no_prime(20, 30))
print(no_prime(24, 25))
print(no_prime(1, 1))
