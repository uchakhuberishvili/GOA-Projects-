def longest_unique_substring(s):
    max_length = 0
    for i in range(len(s)):
        substring = ""
        for j in s[i:]:
            if j in substring:
                break
            substring += j
        max_length = max(max_length, len(substring))
    return max_length

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring(""))
print(longest_unique_substring("pwwkew"))
