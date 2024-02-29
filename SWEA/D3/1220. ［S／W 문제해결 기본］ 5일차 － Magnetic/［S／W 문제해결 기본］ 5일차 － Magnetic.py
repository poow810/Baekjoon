for t in range(10):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if mp[j][i] == 1:
                x = j
                flag_r = True
                break

        for k in range(x+1, 100):
            if flag_r and mp[k][i] == 2:
                count += 1
                flag_r = False

            if (not flag_r) and mp[k][i] == 1:
                flag_r = True
        ans += count

    print(f"#{t+1}", ans)