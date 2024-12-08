def sum_of_positive(numbers):
    total_sum = 0
    for num in numbers:
        if num > 0:
            floored_num = int(num)
            total_sum += floored_num
    return total_sum
print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([-1.5, 2.7, -3.3, 4.8]))
print(sum_of_positive([-1, -2, -3]))
print(sum_of_positive([]))