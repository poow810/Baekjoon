def solution():

    # row
    for i in range(9):
        lst = [x for x in range(1, 10)]
        for j in range(9):
            if mp[j][i] in lst:
                lst.remove(mp[j][i])
            else:
                return 0


    # col
    for i in range(9):
        lst = [x for x in range(1, 10)]
        for j in range(9):
            if mp[i][j] in lst:
                lst.remove(mp[i][j])
            else:
                return 0
    
    # square
    arr = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)]
    for i in arr:
        x, y = i
        lst = [x for x in range(1, 10)]
        for j in range(x, x+3):
            for k in range(y, y+3):
                if mp[j][k] in lst:
                    lst.remove(mp[j][k])
                else:
                    return 0
    return 1


T = int(input())
for t in range(T):
    mp = [list(map(int, input().split())) for _ in range(9)]
    result = solution()

    print(f"#{t+1}", result)