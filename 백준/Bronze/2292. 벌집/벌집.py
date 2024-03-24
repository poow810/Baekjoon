import sys

n = int(sys.stdin.readline())

check = 1  
cnt = 1
while n > check :
    check += 6 * cnt 
    cnt += 1
print(cnt)