import sys
 
N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

if max(lst) == 0:
    print("SAD")

else:
    result = sum(lst[:X])
    max_value = result
    count = 1
    for i in range(X, N):
        result -= lst[i-X]
        result += lst[i]

        if result > max_value:
            max_value = result
            count = 1
        
        elif result == max_value:
            count += 1

    print(max_value)
    print(count)