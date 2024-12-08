def get_common_elements(list1, list2):
    intersection = []
    for num in list1:
        if num in list2 and num not in intersection:
            intersection.append(num)
    return intersection

print(get_common_elements([1, 2, 3], [2, 3, 4]))
print(get_common_elements([1, 1, 2], [1, 3]))
print(get_common_elements([], [1, 2]))
