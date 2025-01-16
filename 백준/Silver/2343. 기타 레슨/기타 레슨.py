import sys

def binary_search(start, end):
    global answer

    while start <= end:
        mid = (start + end) // 2

        count = 1
        add = 0

        for i in lst:
            if add + i > mid:
                count += 1
                add = 0
            add += i
        
        if count <= M:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1


N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

total = sum(lst)
min_count = max(lst)
answer = 0

binary_search(min_count, total)
print(answer)