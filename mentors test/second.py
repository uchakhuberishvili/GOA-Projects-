#2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
def longest_common_prefix(sts):
    if not sts:
        return ""
    sts.sort()
    first = sts[0]
    last = sts[-1]
    i = 0
    prefix = ""
    while i < len(first) and i < len(last):
        if first[i] == last[i]:
            prefix += first[i]
            i += 1
        else:
            break
    return prefix
print(longest_common_prefix(["flower","flow","flight"]))