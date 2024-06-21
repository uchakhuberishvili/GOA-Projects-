def word_search(query, seq):
    if query == " ":
        return ['None']
    result = []
    for word in seq:
        if query.lower() in word.lower():
            result.append(word)
    if not result:
        return ['None']
    return result

def reverse_words(text):
    words_list = text.split(" ")
    reversed_words = []
    
    for word in words_list:
        reversed_words.append(word[::-1])
    
    return " ".join(reversed_words)

