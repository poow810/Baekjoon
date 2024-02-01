T = int(input())

for t in range(T):
    N = int(input())

    c = [0]*5001

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            c[j] += 1
    
    P = int(input())
    ans = []
    for k in range(P):
        C = int(input())
        ans.append(c[C])

    print(f"#{t+1}", " ".join(map(str, ans)))