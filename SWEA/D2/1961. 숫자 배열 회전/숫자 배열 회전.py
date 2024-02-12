T = int(input())
for t in range(T):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]

    
    def one():

        lst = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N-1, -1, -1):
                lst[i].append(mp[j][i])

        return lst
    
    def two():

        lst = [[] for _ in range(N)]
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                lst[N-1-i].append(mp[i][j])
        
        return lst
    
    def three():

        lst = [[] for _ in range(N)]
        for i in range(N-1, -1, -1):
            for j in range(N):
                lst[N-1-i].append(mp[j][i])
        
        return lst

    lst1 = one()
    lst2 = two()
    lst3 = three()
    
    print(f"#{t+1}")
    for k in range(N):
        print("".join(map(str, lst1[k])), "".join(map(str, lst2[k])), "".join(map(str, lst3[k])))
