def solution(arr):

    count = [0]*4
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "#":
                if (i + j) % 2 == 0:
                    count[0] += 1 # 짝수에 #
                else:
                    count[1] += 1 # 홀수에 #
            
            elif arr[i][j] == ".":
                if (i+j) % 2 == 0: 
                    count[2] += 1 # 짝수에 .
                else:            
                    count[3] += 1 # 홀수에 .
    
    if (count[0] and count[1]) or (count[0] and count[2]) or (count[1] and count[3]) or (count[2] and count[3]):
        result = "impossible"
        return result
    else:
        result = "possible"
        return result

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input().strip())

    result = solution(arr)
    print(f"#{i+1}", result)