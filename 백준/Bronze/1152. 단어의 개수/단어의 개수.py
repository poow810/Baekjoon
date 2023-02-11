def word_count(word):
    word = word.split()
    return len(word)


english = input()
print(word_count(english))
