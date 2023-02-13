def count_alpa(word_list, croa_list):
    count = 0
    for j in word_list:
        if j in croa_list:
            croa_list = croa_list.replace(j, '0')   # word_list의 원소가 croa_list안에 있을 때 문자열 제거를 통해
    count = count + len(croa_list)                  # 문자열 길이 return
    return count

croa = input()
word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

print(count_alpa(word, croa))
