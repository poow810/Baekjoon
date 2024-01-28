import sys

def solution(num):

    start = 0
    result = []
    answer = []
    count = 0

    def dfs(start, count):
        
        if count == 6:  # 종료 조건
            if len(result) == 6:
                answer.append(result.copy()) # 그냥 result를 append하면 
                                             # result pop 할 때마다 answer도 바뀜
            else:
                return

        for i in range(start, len(num)):  # 숫자 하나씩 빼면서 모든 경우의 수 탐색
            result.append(num[i])
            dfs(i + 1, count + 1)
            result.pop()

    dfs(start, count)
    return answer
while True:

    num = list(map(int, sys.stdin.readline().split()))
    if len(num) == 1 and num[0] == 0:
        break
    k = num.pop(0)
    answer = solution(num)
    for i in answer:
        print(" ".join(map(str, i)))
    print()

