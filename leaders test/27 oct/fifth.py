# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def palindrome(s):
    cl = ""
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9':
            cl += i.lower() if 'A' <= i <= 'Z' else i
    return cl == cl[::-1]
print(palindrome("A man a plan a canal Panama"))