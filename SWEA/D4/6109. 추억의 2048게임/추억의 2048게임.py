T = int(input())
for t in range(T):
    N, a = map(str, input().split())
    n = int(N)
    mp = [list(map(int, input().split())) for _ in range(n)]
    
    def up():
        
        cnt = 0
        while cnt < n:
            for i in range(n-1, 0, -1):
                    for j in range(n):
                        if mp[i][j] != 0 and mp[i-1][j] == 0:
                            mp[i][j], mp[i-1][j] = mp[i-1][j], mp[i][j]
            cnt += 1

        for k in range(n-1):
            for z in range(n):
                if mp[k][z] == mp[k+1][z]:
                    mp[k][z] += mp[k+1][z]
                    mp[k+1][z] = 0

        count = 0
        while count < n:
            for i in range(n-1, 0, -1):
                for j in range(n):
                    if mp[i][j] != 0 and mp[i-1][j] == 0:
                        mp[i][j], mp[i-1][j] = mp[i-1][j], mp[i][j]
            count += 1  # 0이 없을 때까지 계속 자리 바꿈

        return mp

    def down():

        cnt = 0
        while cnt < n:
            for i in range(n-1):
                    for j in range(n):
                        if mp[i][j] != 0 and mp[i+1][j] == 0:
                            mp[i][j], mp[i+1][j] = mp[i+1][j], mp[i][j]
            cnt += 1

        for k in range(n-1, 0, -1):
            for z in range(n):
                if mp[k][z] == mp[k-1][z]:
                    mp[k][z] += mp[k-1][z]
                    mp[k-1][z] = 0

        count = 0
        while count < n:
            for i in range(n-1):
                for j in range(n):
                    if mp[i][j] != 0 and mp[i+1][j] == 0:
                        mp[i][j], mp[i+1][j] = mp[i+1][j], mp[i][j]
            count += 1  # 0이 없을 때까지 계속 자리 바꿈
        return mp

    
    def right():
        
        cnt = 0
        while cnt < n:
            for i in range(n):
                for j in range(n-1, 0, -1):
                    if mp[i][j] == 0 and mp[i][j-1] != 0:
                        mp[i][j-1], mp[i][j] = mp[i][j], mp[i][j-1]
            cnt += 1

        for k in range(n-1, 0, -1):
            for z in range(n):
                if mp[z][k] == mp[z][k-1]:
                    mp[z][k] += mp[z][k-1]
                    mp[z][k-1] = 0

        count = 0
        while count < n:
            for i in range(n):
                for j in range(n-1, 0, -1):
                    if mp[i][j] == 0 and mp[i][j-1] != 0:
                        mp[i][j-1], mp[i][j] = mp[i][j], mp[i][j-1]
            count += 1  # 0이 없을 때까지 계속 자리 바꿈
        return mp

    
    def left():

        cnt = 0
        while cnt < n:
            for i in range(n):
                for j in range(n-1):
                    if mp[i][j] == 0 and mp[i][j+1] != 0:
                        mp[i][j+1], mp[i][j] = mp[i][j], mp[i][j+1]
            cnt += 1

        for k in range(0, n-1):
            for z in range(n):
                if mp[z][k] == mp[z][k+1]:
                    mp[z][k] += mp[z][k+1]
                    mp[z][k+1] = 0

        count = 0
        while count < n:
            for i in range(n):
                for j in range(n-1):
                    if mp[i][j] == 0 and mp[i][j+1] != 0:
                        mp[i][j+1], mp[i][j] = mp[i][j], mp[i][j+1]
            count += 1  # 0이 없을 때까지 계속 자리 바꿈
        return mp
    
    if a == "up":
        print(f"#{t+1}")
        mp = up()
        for i in mp:
            print(" ".join(map(str, i)))
    elif a == "down":
        print(f"#{t+1}")
        mp = down()
        for i in mp:
            print(" ".join(map(str, i)))
    elif a == "left":
        print(f"#{t+1}")
        mp = left()   
        for i in mp:
            print(" ".join(map(str, i)))
    elif a == "right":
        print(f"#{t+1}")
        mp = right()
        for i in mp:
            print(" ".join(map(str, i)))
