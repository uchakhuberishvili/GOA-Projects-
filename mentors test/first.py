#Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.

def find_missing_number(arr,n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number
print(find_missing_number([1,2,3,4,5,7,8,9,10],10))