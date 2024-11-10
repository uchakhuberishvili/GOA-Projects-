#3. Given an array of size n, find the majority element.
#  The majority element is the element that appears more than n // 2 times.
#  You may assume that the array is non-empty and the majority element always exists in the array.
def majority(n):
    m_count = len(n)//2
    for i in n:
        count = n.count(i)
        if count > m_count:
            return i
print(majority([2, 2, 1, 1, 2]))