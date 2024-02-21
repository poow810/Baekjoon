T = int(input())
for _ in range(T):
    t = int(input())
    lst = list(map(int, input().split()))
    dic = {}

    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    max_c = 0
    max_idx = 0
    for key, value in dic.items():
        if max_c <= value:
            max_c = value
    
    for i in dic:
        if dic[i] == max_c:
            if max_idx < int(i):
                max_idx = int(i)

    
    print(f"#{t}", max_idx)
