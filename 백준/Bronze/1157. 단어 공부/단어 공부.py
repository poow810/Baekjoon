def letter(words):
    letter_dict = {}
    for i in words:
        if i in letter_dict:
            letter_dict[i] +=1 # 중복 문자가 있다면 그 만큼의 합
        else:
            letter_dict[i] = 1 # 중복 문자가 없다면 개수 : 1
    return letter_dict


words= input()
word = letter(words.upper())

max_value = max(word.values())
max_keys = [k for k, v in word.items() if v == max_value]

if len(max_keys) == 1:
    print(''.join(max_keys))
else:
    print('?')



