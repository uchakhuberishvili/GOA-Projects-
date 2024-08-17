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