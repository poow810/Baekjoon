import sys


def min_search(num):

    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    
    return end + 1


def max_search(num):

    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

for _ in range(M):
    count = 0
    a, b = map(int, sys.stdin.readline().split())
    print(max_search(b) - min_search(a)+1)