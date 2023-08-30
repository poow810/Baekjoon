import sys

A, B = map(int, sys.stdin.readline().split())

# 최대 공약수
def gcd(A, B):
    while B:
        A, B = B, A%B
    return A

# 최소 공배수
max_num = (A*B)//gcd(A, B)

print(gcd(A, B))
print(max_num)