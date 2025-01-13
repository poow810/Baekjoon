import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    Ti, *lst = map(int, sys.stdin.readline().split())

    dic = dict()
    for i in lst:
        if i in dic:
            dic[i] += 1
            if dic[i] > Ti // 2:
                print(i)
                break
        else:
            dic[i] = 1
    
    else:
        print("SYJKGW")    
