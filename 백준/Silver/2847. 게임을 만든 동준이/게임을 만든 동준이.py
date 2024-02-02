import sys
N = int(sys.stdin.readline())

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

count = 0
valid = False
while True:
    for j in range(len(lst) - 1):
        if lst[j] >= lst[j+1]:
            lst[j] -= 1
            count += 1

    for k in range(len(lst)-1):
        if lst[k] < lst[k+1]:
            valid = True
        else:
            valid = False
            break
    
    if valid:
        break


print(count)