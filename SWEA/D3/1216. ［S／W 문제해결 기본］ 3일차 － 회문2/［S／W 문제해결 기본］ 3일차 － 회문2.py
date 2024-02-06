for t in range(10):
    M = int(input())
    lst = [list(input()) for _ in range(100)]
    N = 100

    def solution(M):

        for i in range(N):
            for j in range(N-M+1):
                for k in range(M//2):
                    if lst[i][j+k] != lst[i][M+j-k-1]:
                        break
                
                else:
                    return M

            for j in range(N-M+1):
                for k in range(M//2):
                    if lst[j+k][i] != lst[M+j-k-1][i]:
                        break
            
                else:
                    return M

    max_num = 0
    for i in range(100):
        if solution(i) != None:
            ans = solution(i)
            if max_num < ans:
                max_num = ans
    

    print(f"#{t+1}", max_num)