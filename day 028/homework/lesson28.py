
def overall(num):
    if num < 0:
        return 0
    else:
        ssum = 0
        for i in range(num):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum

#Example usage:
number = 10
result = overall(number)
print(result)



def trueorfalse(string1,string2):
    if string2 in string1:
        return True
    else:
        return False
results = trueorfalse("hidroeleqtrosadguri","eleqtro")
print(results)



def mathematics(operator,value1,value2):
    if operator == "+":
        res = value1 + value2
    elif operator == "-":
        res = value1 - value2
    elif operator == "//":
        res = value1 // value2
    elif operator == "*":
        res = value1 * value2
    print(res)
    return res
mathematics("*",178,9)

def lowest(list1):

    smallest = list1[0]

    for i in list1:
        if i < smallest:

            smallest = i
        
        return smallest
        

list1 = [10,7,98,123]

list2 = [84,91,657,234,76]

resulttt = list1 + list2
print(lowest(resulttt))


