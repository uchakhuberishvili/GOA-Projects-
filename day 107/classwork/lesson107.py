

def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word



def find_longest_word_hard(s):
    words = s.split()
    longest_word = max(words, key=lambda x: sum(ord(c) for c in x))
    return longest_word
