import sys

N = int(sys.stdin.readline().strip())
lst = []
answer = 0

for N in range(N):
    check, *input = map(int, sys.stdin.readline().split())

    if input:
        score, time = input[0], input[1]

    if check == 0:
        if lst:
            if lst[-1][1] == 0:
                answer += lst[-1][0]
                lst.pop()
            lst[-1][1] -= 1
            if lst[-1][1] == 0:
                answer += lst[-1][0]
                lst.pop()
        continue

    lst.append([score, time])
    lst[-1][1] -= 1
    
    if lst[-1][1] == 0:
        answer += lst[-1][0]
        lst.pop()

print(answer)
