T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    bread = 0
    lst.sort()
    idx = 0
    for i in range(11111):
        if i != 0 and i % M == 0:
            bread += K
        
        if idx >= len(lst):
            print(f"#{t+1}", "Possible")
            break

        if lst[idx] < M:
            print(f"#{t+1}", "Impossible")
            break
        
        if lst[idx] == i:
            bread -= 1
            if bread < 0:
                print(f"#{t+1}", "Impossible")
                break
            idx += 1
    else:
        print(f"#{t+1}", "Possible")