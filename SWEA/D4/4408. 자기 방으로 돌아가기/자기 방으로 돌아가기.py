T = int(input())
for t in range(T):
    N = int(input())
    visited = [0]*200
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        
        for i in range((a-1)//2, (b-1)//2 + 1):
            visited[i] += 1
    
    max_num = 0
    for j in visited:
        if max_num < j:
            max_num = j
    
    print(f"#{t+1}", max_num)


    
