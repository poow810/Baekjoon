T = int(input())
for t in range(T):
    mp = [list(map(int, input().split())) for _ in range(9)]

    def col():

        valid = False
        for i in range(9):
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if mp[j][i] in lst:
                    lst.remove(mp[j][i])
                else:
                    return False
            
            if not lst:
                valid = True
        
        return valid


    def row():

        valid = False
        for i in range(9):
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if mp[i][j] in lst:
                    lst.remove(mp[i][j])
                else:
                    return False
                
            if not lst:
                valid = True
            
        return valid
    

    def block():
        
        check = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                 (3, 6), (6, 0), (6, 3), (6, 6)]
        valid = False

        for k in check:
            x, y = k
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if mp[j][i] in lst:
                        lst.remove(mp[j][i])
                    else:
                        return False
                
            if not lst:
                valid = True

        return valid

    if col() and row() and block():
        print(f"#{t+1}", 1)
    else:
        print(f"#{t+1}", 0)
