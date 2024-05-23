def manual_index1(numbers_list,search_value):
    return numbers_list[search_value]
print(manual_index1([10,20,30,40],3))

def manual_index2(numbers_list,search_value):
    for i in numbers_list:
        if i == search_value:
            print("your number is " + str(numbers_list[i]))
manual_index2([1,7,8,2,5,6],5)

def manual1(manual_max,manual_min):
    sort1 =  sorted(manual_max)
    Len = len(manual_max)
    sort2 = sorted(manual_min)
    return sort1[Len - 1] , sort2[0]
print(manual1([10,20,30,5],[10,20,12,5]))

def manual2(manual_max, manual_min):
    max_value = max(manual_max)
    min_value = min(manual_min)
    return max_value, min_value

print(manual2([10, 20, 30, 5], [10, 20, 12, 5]))
    
def manual_pop(List,poper):
    lis2 = []
    lis = List.pop(poper)
    for i in List:
        if i != lis:
            lis2.append(i)
    return lis2
print(manual_pop([10,20,30,40,50],4))
