def anagrams(txt1, txt2):
    return sorted(txt1) == sorted(txt2)

print(anagrams("listen", "silent"))
print(anagrams("hello", "world"))
print(anagrams("triangle", "integral"))
