def one_number():
    N = int(input())
    count = 0
    add = 0
    if N < 100:
        for j in range(0, N):
            add+=1
    if 1000>=N>=100:
        for i in range(100, N+1):
            if (i // 100 - (i // 10) % 10) == ((i // 10) % 10 - i % 10):
                count += 1
        for K in range(1, 100):
            add+=1
    print(add+count)
one_number()