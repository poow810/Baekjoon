import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
x = int(sys.stdin.readline().strip())

left, right = 0, N-1
count = 0
while left != right:

    if lst[left] + lst[right] == x:
        count += 1
        left += 1
    elif lst[left] + lst[right] > x:
        right -= 1
    else:
        left += 1

print(count)