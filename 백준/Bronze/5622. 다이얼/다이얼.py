def count_time(words_list, alpa):
    count = 0
    for i in range(len(words_list)):
        for j in alpa:
            if words_list[i] in j:
                count = count + alpa.index(j)+3
    return count


word = input()
words = list(word)
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


print(count_time(words, alphabet))


# 간단하게 리스트로 문자열을 받고,
# for문을 통해 리스트 순회
# 같은 값을 찾아줌