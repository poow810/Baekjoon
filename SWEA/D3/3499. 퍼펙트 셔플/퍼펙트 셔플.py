from collections import deque

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(str, input().split()))
    lst2 = []
    n = N // 2
    ans = []
    if N % 2 == 0:
        lst2 = lst[n:]
        for i in range(n):
            ans.append(lst[i])
            ans.append(lst2[i])
    else:
        lst2 = lst[n+1:]
        for i in range(n):
            ans.append(lst[i])
            ans.append(lst2[i])
        ans.append(lst[n]) 
    
    print(f"#{t+1}", " ".join(ans))