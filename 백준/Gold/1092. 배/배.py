import sys
from collections import deque

def binary_search(target):

    start, end = 0, len(boxes)

    while start < end:
        mid = start + (end - start) // 2
        if boxes[mid] <= target:
            start = mid + 1
        else:
            end = mid
    
    return end
    

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().split()))

lst.sort()
boxes.sort()

if lst[-1] < boxes[-1]:
    print(-1)
    exit()

count = 0

while boxes:
    if not boxes:
        break

    count += 1
    for i in lst:
        if not boxes:
            break

        index = binary_search(i)
        if boxes:
            if index == 0:
                continue
            else:
                boxes.pop(index-1)

print(count)