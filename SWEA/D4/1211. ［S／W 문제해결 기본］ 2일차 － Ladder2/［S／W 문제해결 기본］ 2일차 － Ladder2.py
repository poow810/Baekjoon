for t in range(10):
    T = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]

    y_lst = []
    for i in range(100):
        if mp[99][i] == 1:
            y_lst.append(i)

    # 강사님 풀이
    # 방향을 계속 바꿔줘야하는 로직에서는 dx dy보다는
    # m, u, l, r 쓰기 -> 직접 방향 설정이 쉬움
    ans = 0
    min_num = 999999

    for y in y_lst:

        x = 99
        count = 0
        m, u, l, r = 0, 0, 1, 2

        # 0일 때까지 반복
        while x > 0:
            # 왼쪽 벽과 만나거나, 1일 때 (위나 왼쪽 탐색)
            if y > 0 and mp[x][y-1] == 1 and (m == u or m == l):
                y -= 1
                m = l
            
            elif y < 99 and mp[x][y+1] == 1 and (m == u or m ==r):
                y += 1
                m = r
            
            elif mp[x-1][y] == 1:
                x -= 1
                m = u
            
            # x 이동 횟수는 동일, y 이동 횟수만 세면 됨
            if m == l or m == r:
                count += 1
        
        if min_num > count:
            min_num = count
            ans = y
    
    print(f"#{t+1}", ans)

