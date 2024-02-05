T = int(input())
for t in range(T):

    lst = [list(input()) for _ in range(5)]
    max_len = 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
    ans = []
    a = ""
    for i in range(max_len):
        for j in range(5):
            if not lst[j]:
                continue
            a += lst[j].pop(0)

    print(f"#{t+1}", a)