import sys


def binarySearch(n):
    global ans, r, c

    if n == 0:
        return

    n -= 1
    size = 2**n

    if r < size and c < size: # 1 사분면
        binarySearch(n)

    elif r < size and c >= size: # 2 사분면
        ans += size*size
        c -= size
        binarySearch(n)
        
    elif r >= size and c < size: # 3 사분면
        ans += size*size*2
        r -= size
        binarySearch(n)

    elif r >= size and c >= size: # 4 사분면
        ans += size*size*3
        r -= size
        c -= size
        binarySearch(n)


N, r, c = map(int, sys.stdin.readline().split())
ans = 0
binarySearch(N)
print(ans)
