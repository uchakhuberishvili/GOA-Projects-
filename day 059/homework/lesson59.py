def find_uniq(arr):
    result = ""
    l = arr[0]
    for i in arr:
        if i != l:
            result += str(i)
    return int(result)
print(find_uniq([1,1,1,1,3,1,1]))


def simple_multiplication(number) :
    if number % 2 ==0:
        return number * 8
    else:
        return number * 9
    

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]
    
def billboard(name, price=30):
    total_price = 0
    for i in name:
        total_price += price
    return total_price
print(billboard("ucha"))


def square(n):
    if n == str:
        return 0
    return n * n