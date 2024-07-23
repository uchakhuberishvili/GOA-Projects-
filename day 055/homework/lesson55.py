def filter_list(l):
    nlist = []
    for i in l:
        if type(i) == int:
            nlist.append(i)
    return nlist
print(filter_list([12,56,234,"hello","good!"]))



def positive_sum(arr):
    Sum = 0
    for i in arr:
        if i > 0:
            Sum += i
    return Sum
print(positive_sum([-10,20,30,-15,123,45]))


def count_positives_sum_negatives(arr):
    negatives = 0
    positives = 0
    for i in arr:
        if i >= 0:
            positives += 1
        elif i < 0:
            negatives += i
    return [positives,negatives]
print(count_positives_sum_negatives([1,3,2,3,4,-5,-10,-3,-123]))

def remove_char(s):
    return s[1:-1]
print(remove_char("hello"))


def make_negative(number):
    number = str(number)
    neg = "-" + number
    if "-" in number:
        return int(number)
    neg = int(neg)
    return neg
print(make_negative(20))