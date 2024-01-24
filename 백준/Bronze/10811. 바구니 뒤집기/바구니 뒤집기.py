import sys

def solution(basket, a, b):

    rv_basket = list(reversed(basket[a-1:b]))
    new_basket = basket[0:a-1] + rv_basket + basket[b:]
    return new_basket


N, M = map(int, sys.stdin.readline().split())
basket = [x for x in range(1, N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    basket = solution(basket, a, b)

print(' '.join(map(str, basket)))