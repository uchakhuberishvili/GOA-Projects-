def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    sum_lowest = numbers[0] + numbers[1]
    return sum_lowest
print(sum_two_smallest_numbers([12,4,123,45,76,5]))


def max_multiple(divisor, bound):
    return (bound // divisor) * divisor
print(max_multiple(2,7))

def get_even_numbers(arr):
    even = []
    for i in arr:
        if i % 2 ==0:
            even.append(i)
    return even

def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score +=4
        elif arr2[i] == "":
            score = score
        else:
            score -=1
    if score <=0:
        score =0
    return score


def row_weights(array):
    first_row = []
    second_row = []
    rows = [first_row,second_row]
    overall = []
    for i in range(0, len(array), 2):
        first_row.append(i)
    for i in range(1, len(array), 2):
        second_row.append(i)
    overall.append(rows)
    return overall

def human_years_cat_years_dog_years(human_years):
    catyears = 0
    dogyears = 0
    for i in human_years:
        if i ==1:
            catyears += 15
            dogyears += 15
        elif i == 2:
            catyears += 9
            dogyears += 9
        elif i >=3:
            catyears += 4
            dogyears += 5
    result = [human_years,catyears,dogyears]
    return result


def spot_diff(s1, s2):
    if s1 == s2:
        return []
    
    difference_indexes = []
    
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            difference_indexes.append(index)
    
    return difference_indexes