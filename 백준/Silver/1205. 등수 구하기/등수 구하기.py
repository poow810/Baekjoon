import sys

N, score, P = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
answer = 0
if lst:
    if score >= lst[0]:
        answer = 1

flag = True
for i in range(N):
    if lst[i] == score:
        if i+1 == N:
            if i+1 >= P:
                answer = -1
        flag = False
    if lst[i] > score:
        if flag == False:
            answer = i
        answer = i+2
        if i+1 >= P:
            answer = -1

if len(lst) == 0:
    print(1)
else:
    print(answer)
        