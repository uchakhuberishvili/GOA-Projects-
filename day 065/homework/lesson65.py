def find_uniq(arr):
    result = ""
    l = arr[0]
    for i in arr:
        if i != l:
            result += str(i)
    return int(result)
print(find_uniq([1,1,1,1,3,1,1]))



def reverse_seq(n):
    result = []
    for i in range(n,0,-1):
        result.append(i)
    return result


def odd_or_even(arr):
    full = 0
    for i in arr:
        full += i
    if full % 2 == 0:
        return "even"
    else:
        return "odd"
    
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)



def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]