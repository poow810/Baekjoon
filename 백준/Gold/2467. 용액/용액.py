import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(lst) - 1
answer_left, answer_right = 0, 0
count = 1e99  

while left < right:  
    check = lst[left] + lst[right]

    if abs(check) < abs(count):
        count = check
        answer_left = lst[left]
        answer_right = lst[right]

    if check > 0:
        right -= 1
    elif check < 0:
        left += 1
    else: 
        break

print(answer_left, answer_right)
