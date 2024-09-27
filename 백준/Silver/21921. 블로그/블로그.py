import sys

N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

if sum(lst) == 0:
    print("SAD")
else:   
    res = sum(lst[:X])
    max_value = res
    count = 1

    for i in range(X, len(lst)):
        res += lst[i]
        res -= lst[i-X]

        if res > max_value:
            max_value = res
            count = 1
    
        elif res == max_value:
            count += 1

    print(max_value)
    print(count)
