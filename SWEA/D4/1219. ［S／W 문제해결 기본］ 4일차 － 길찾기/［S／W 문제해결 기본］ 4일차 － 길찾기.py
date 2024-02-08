for _ in range(10):
    t, road = map(int, input().split())
    lst = list(map(int, input().split()))
    mp = [[] for _ in range(100)]
    for i in range(road):
        n1, n2 = lst[i*2], lst[i*2+1]
        mp[n1].append(n2)
        mp[n2].append(n1)
    
    start = 0

    def dfs(start):


        stack = [start]
        visited = [0] * (100)
        while stack:
            count = 0
            current = stack.pop()
            if visited[current] == 1:
                continue

            if visited[current] == 0:
                visited[current] = 1

            for i in reversed(mp[current]):
                if visited[i] == 0:
                    stack.append(i)
                    count += 1
                
                if count >= 2:
                    break
            
        if visited[99] == 1:
            return 1
        else:
            return 0


    print(f"#{t}", dfs(0))