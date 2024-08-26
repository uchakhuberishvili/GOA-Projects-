def min_max(lst):
    result = []
    minim = min(lst)
    maxim = max(lst)
    result.append(minim)
    result.append(maxim)
    return result

def create_array_of_tiers(n):
    str_n = str(n)
    result = []

    for i in range(1, len(str_n) + 1):
        result.append(str_n[:i])
    return result