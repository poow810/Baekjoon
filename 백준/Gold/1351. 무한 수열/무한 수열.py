import sys

def solution(n):

    if (n in dict):
        return dict[n]
    else:
        dict[n] = solution(n//p) + solution(n//q)
        return dict[n]

n, p, q = map(int, sys.stdin.readline().split())

dict = {}
dict[0] = 1

print(solution(n))