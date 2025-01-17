import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

left, right = 0, N - 1
answer = 1e99
ans_lst = [0, 0]

while left < right:
    total = lst[left] + lst[right]

    if answer > abs(total):
        answer = abs(total)
        ans_lst[0], ans_lst[1] = lst[left], lst[right]
    
    if total > 0:
        right -= 1
    else:
        left += 1

print(ans_lst[0], ans_lst[1])