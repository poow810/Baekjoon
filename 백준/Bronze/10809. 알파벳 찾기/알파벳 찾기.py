import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = sys.stdin.readline()

for i in alphabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')


# alphabet 문자열을 지정 후 else로 나머지 문자 처리