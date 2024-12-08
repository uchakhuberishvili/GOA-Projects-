def positives(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res
print(positives([1, -4, 7, 12]))
print(positives([-1, -2, -3, -4]))
print(positives([]))