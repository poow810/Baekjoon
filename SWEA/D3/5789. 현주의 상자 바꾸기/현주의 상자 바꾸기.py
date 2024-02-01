T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    lst = [0] * N

    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            lst[j-1] = i
    
    print(f"#{t+1}", " ".join(map(str, lst)))