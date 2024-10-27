# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']
def remove_extra(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res
print(remove_extra([1, 2, 2, 3, 4, 4, 5]))