import sys


def solution(num):

    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
else:
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline().rstrip()))

    lst.sort()
    idx = solution(n * 0.15)
    print(solution(sum(lst[idx:n-idx])/len(lst[idx:n-idx])))