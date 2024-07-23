def if_chuck_says_so():
    return 1 > 2

def two_oldest_ages(ages):
    Sort = sorted(ages)
    Len = Sort[-1,-2]
    return Len

def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    oldest_ages = sorted_ages[-2:]
    return oldest_ages