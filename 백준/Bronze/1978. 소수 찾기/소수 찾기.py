import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in num_list:
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            break
    else:    
        count += 1
print(count)
