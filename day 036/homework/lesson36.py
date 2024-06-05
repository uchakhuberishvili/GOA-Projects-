def abbrev_name(name):
    count = 0
    inittials = ("")
    inittials += name[0]
    inittials += (".")
    capped = []
    final = ""
    for i in name:
        if i != " ":
            count += 1
        if i == " ":
            i = count + 1
            inittials += (name[i])
    for i in inittials:
        capped.append(i.capitalize())
    for i in capped:
        final += i
    return final
print(abbrev_name("ucha khubera"))

def sum_mix(arr):
    result = 0
    for i in arr:
        i = int(i)
        result += i
    return result


def find_smallest_int(arr):
    arr = sorted(arr)
    return arr[0]
print(find_smallest_int([78, 56, 232, 12, 11, 43]))



def count_sheep(n):
    count = ""
    for i in range(1,n+1):
        count += str(i) + " sheep..."
    return count
print(count_sheep(5))


def array_plus_array(arr1,arr2):
    result = 0
    for i in arr1:
        result += i
    for i in arr2:
        result += i
    return result

#def all_nines(x):
#    result = 0
#    for i in range(0,1000):
#        if x * i == 9 or 99 or 999:
#            result += i
#    return result
#print(all_nines(13))