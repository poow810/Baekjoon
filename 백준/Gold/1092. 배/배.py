import sys
from collections import deque

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().split()))

lst.sort(reverse=True)
boxes.sort(reverse=True)


answer = 0

if boxes[0] > lst[0]:
    print(-1)
    exit()

while boxes:

    answer += 1
    for i in lst:

        if boxes and i < boxes[-1]:
            continue
        for j in boxes:
            if i >= j and boxes:
                boxes.remove(j)
                break

print(answer)
