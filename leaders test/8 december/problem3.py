def find_missing_number(numbers):
    n = len(numbers) + 1
    missing = 1
    while missing <= n:
        if missing not in numbers:
            return missing
        missing += 1
print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([3, 5, 6, 1, 2]))
print(find_missing_number([2]))