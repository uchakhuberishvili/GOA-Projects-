def Num_list(List):
    even = []
    for i in List:
        if i % 2 ==0:
            even.append(i)
    i = len(even)
    return i
print(Num_list([1,3,5,2,6,66,22,32,44]))


def List(List):
    count = 0
    for i in List:
        count += 1
    return count
print(List([123,23,34,435,456,78,986,67,435,76]))


def four(List):
    Sum = 0
    for i in List:
        if i % 4 ==0:
            Sum += i
    return Sum
print(four([1,2,3,4,5,6,7,8,9,10,11,12]))

def manual_count(List):
    u = int(input("enter a number: "))
    count = 0
    for i in List:
        if i ==u:
            count += 1
    return count
print(manual_count([1,2,3,4,5,6,7,8,9,10,10,10,9,3]))