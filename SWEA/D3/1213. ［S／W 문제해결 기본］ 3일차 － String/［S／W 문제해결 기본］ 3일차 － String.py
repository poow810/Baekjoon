for t in range(10):
    T = int(input())
    check = input()
    string = input()
    n = len(string)
    m = len(check)
    i = 0
    count = 0

    while i <= n - m:
        found = True
        for j in range(0, m):
            if string[i+j] != check[j]:
                found = False
                break
        if found:
            count += 1
            i += m
            continue
        i += 1

    print(f"#{T}", count)