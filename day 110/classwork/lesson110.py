from collections import Counter

def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p) - 1])

    for i in range(len(p) - 1, len(s)):
        s_count[s[i]] += 1

        if s_count == p_count:
            result.append(i - len(p) + 1)

        s_count[s[i - len(p) + 1]] -= 1
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]

    return result

print(find_anagrams("cbaebabacd", "abc"))

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3, 2, 1, 5, 6, 4], 2))

