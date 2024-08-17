def check_int(num):
    if num % 2 == 0:
        return str(num) + " is Even"
    else:
        return str(num) + " is Odd"


print(check_int(6))




def check_if_prime(num):
    if num == 2:
        return str(num) + " is prime"
    if num <= 1:
        return str(num) + " is invalid number"
    
    count = 2
    
    for i in range(2, num):
        if num % i == 0:
            count = count + 1
        if count > 2:
            return str(num) + ' is not prime'
    
    return str(num) + ' is prime'

print(check_if_prime(5))

