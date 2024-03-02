from collections import deque

T = int(input())
for t in range(T):
 
    lst = [deque(input()) for _ in range(5)]
    max_len = 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
    a = ""
    for i in range(max_len):
        for j in range(5):
            if not lst[j]:
                continue
            a += lst[j].popleft()
 
    print(f"#{t+1}", a)