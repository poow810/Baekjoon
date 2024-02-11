T = int(input())
for t in range(T):
    N = int(input())
    mp = [[0]*N for _ in range(N)]
    y = N//2
    for i in range(N):
        lst = list(map(int, input()))
        
        if y >= i:
            for k in range(abs(y-i), abs(y+i)+1):
                mp[i][k] = lst[k]
        elif y < i:
            for k in range(abs(y-i), N+y-i):
                mp[i][k] = lst[k]
    count = 0
    for j in mp:
        for k in j:
            if k != 0:
                count += k
    print(f"#{t+1}", count)