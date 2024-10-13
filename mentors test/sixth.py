#6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.

def two_sumed(a,b):
    comb = a + b
    comb.sort()
    return sum(comb) / len(comb)
print(two_sumed([10, 20], [30, 40, 50]))