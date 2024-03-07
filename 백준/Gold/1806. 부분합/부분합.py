import sys

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
add = 0
min_add = 1e99

while True:
    if add >= S:
        length = start - end
        if min_add > length:
            min_add = length
    
        add -= lst[end]
        end += 1

    elif start == N:
        break
    
    else:
        add += lst[start]
        start += 1
        
 

if min_add == 1e99:
    print(0)
else:
    print(min_add)

