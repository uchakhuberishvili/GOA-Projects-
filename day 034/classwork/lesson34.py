def Num_list(List):
    even = []
    for i in List:
        if i % 2 ==0:
            even.append(i)
    i = len(even)
    return i
print(Num_list([1,3,5,2,6,66,22,32,44,65]))


def List(List):
    count = 0
    for i in List:
        count += i
    return count
print(List([123,23,34,435,456,78,986,67,435,76]))


