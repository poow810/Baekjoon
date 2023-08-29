import sys

count = 1
for i in range(3):
    a = int(sys.stdin.readline())
    count *= a
count_str = str(count)
dict = {str(i): 0 for i in range(10)}

for j in count_str:
    dict[j] += 1

for value in dict:
    print(dict[value])



# 숫자 -> 문자열 변환
# 딕셔너리에 해당 문자와 value 저장
# 문자열을 돌면서 딕셔너리 키값에 있다면 value += 1
