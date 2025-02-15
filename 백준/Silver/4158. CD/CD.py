import sys


def binary_search(target):
    global count

    left = 0
    right = len(lst_1) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst_1[mid] == target:
            count += 1
            break

        elif lst_1[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    
    lst_1 = [int(sys.stdin.readline().strip()) for _ in range(N)]
    lst_2 = [int(sys.stdin.readline().strip()) for _ in range(M)]

    count = 0

    for i in lst_2:
        binary_search(i)

    print(count)