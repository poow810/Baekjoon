import sys

def binarySearch(number):

    start, end = 0, M-1

    idx = 0

    while start <= end:
        mid = (start + end) // 2
        if B[mid] < number:
            start = mid + 1
            idx = mid
            
        else:
            end = mid - 1

    return idx + 1


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    count = 0

    A.sort()
    B.sort()

    for i in A:
        if i > B[0]:
            count += binarySearch(i)
    print(count)