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

def capitalize_names(names_list):
    formated_list = []
    for name in names_list:
        formated_list.append(name.capitalize())
    return formated_list

print(capitalize_names(["david", "chad", "gigachad"]))



def separate_evens_odds(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number // 2)
        else:
            result.append(number * 2)
    return result


print(separate_evens_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



