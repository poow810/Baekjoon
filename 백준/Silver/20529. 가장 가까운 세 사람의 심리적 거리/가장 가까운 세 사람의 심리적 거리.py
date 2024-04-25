import sys
from itertools import combinations


def solution(a, b):
    x = 0
    for (i, j) in zip(a, b):
        if i != j:
            x += 1
    return x


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    mbti = sys.stdin.readline().rstrip().split()

    if N > 32:
        print(0)
    
    else:
        dist = 13

        for (a, b, c) in combinations(mbti, 3):
            d = 0
            d += solution(a, b)
            d += solution(b, c)
            d += solution(c, a)

            dist = min(dist, d)
            
        print(dist)
