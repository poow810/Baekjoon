T = int(input())
for t in range(T):

    N = int(input())

    # def solution(n):
        
    #     n -= 1
    #     if  n <= 0:
    #         return print(1)
        
    #     solution(n)
    #     return 1 + solution(n)

    # solution(N)
    print(f"#{t+1}")

    mp = [[] for _ in range(N)]
    for i in range(N): # 0, 1, 2, 3
        for j in range(i+1): # 0, 1, 2, 3,
            if j == 0 or j == i or i == 0:
                mp[i].append(1)
            else:
                mp[i].append(mp[i-1][j-1] + mp[i-1][j])
    for j in range(len(mp)):
        print(" ".join(map(str, mp[j])))