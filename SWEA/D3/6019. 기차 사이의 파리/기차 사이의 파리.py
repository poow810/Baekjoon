T = int(input())
for i in range(T):
    D, A, B, F = map(int, input().split())
    
    t = D / (A + B)
    distance = F * t
    
    print(f"#{i+1}", distance)