T = int(input())
dic = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4,
        "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
for t in range(T):
    test, N = input().split()
    lst = list(map(lambda x: dic.get(x), input().split()))

    max_num = 0
    for i in range(int(N)-1):
        max_num = i
        for j in range(i+1, int(N)):
            if lst[j] < lst[max_num]:
                max_num = j
        lst[i], lst[max_num] = lst[max_num], lst[i]
    dic_ch = {}
    for key, value in dic.items():
        dic_ch[value] = key
    ans = list(map(lambda x: dic_ch.get(x), lst))
    
    print(test)
    for i in ans:
        print(i, end = " ")
    print()