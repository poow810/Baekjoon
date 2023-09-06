import sys

def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    
    return result

N = int(sys.stdin.readline())

# 처음 0이 아닌 숫자가 나오는 factorial number 판별
num_list = list(str(factorial(N)))
index = 0
for i in range(len(num_list)-1, 0, -1):
    if num_list[i] != '0':
        index = i
        break


# 0 개수 세기
count = 0

if len(num_list) > 0:
    for k in range(len(num_list)-1, index, -1):    
        if num_list[k] == '0':
            count+= 1
else:
    if num_list[0] == '0':
        count += 1
    else:
        count = 0

print(count)