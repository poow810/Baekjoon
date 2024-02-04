for t in range(10):
    T = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]


    def col():

        max_col = 0
        for i in range(100):
            count_col = 0
            for j in range(100):
                count_col += mp[i][j]
            
            if max_col < count_col:
                max_col = count_col
        return max_col

    def row():

        max_row = 0
        for i in range(100):
            count_row = 0
            for j in range(100):
                count_row += mp[j][i]
            
            if max_row < count_row:
                max_row = count_row
        
        return max_row

    def cross():

        max_cross = 0
        for i in range(100):
            count_cross = 0
            for j in range(100):
                if i == j:
                    count_cross += mp[i][j]
            
            if max_cross < count_cross:
                max_cross = count_cross

        return max_cross
        
    
    ans = []
    ans.append(col())
    ans.append(row())
    ans.append(cross())

    max_ans = 0
    for i in ans:
        if max_ans < i:
            max_ans = i

    print(f"#{t+1}", max_ans)
