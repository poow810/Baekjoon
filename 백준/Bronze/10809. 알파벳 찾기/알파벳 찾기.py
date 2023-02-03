S = input()
alphabet = list(range(97, 123))  #아스키코드 숫자 범위
for i in alphabet:
    print(S.find(chr(i)))  # find함수 있으면 첫 번째 index,
                            # 없다면 -1 반환