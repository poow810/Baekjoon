import sys

N = int(sys.stdin.readline().strip())
switch = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 1: # 남자
        check = N // b
        for i in range(1, check+1):
            if switch[i*b-1] == 0:
                switch[i*b-1] = 1
            else:
                switch[i*b-1] = 0

    elif a == 2: # 여자
        idx = 1
        while True:
            flag = False
            if b-idx-1==-1 or b+idx-1==N:
                break
            if switch[b-idx-1] == 0 and switch[b+idx-1] == 0:
                idx += 1
                flag = True
                continue
            if switch[b-idx-1] == 1 and switch[b+idx-1] == 1:
                idx += 1
                flag = True
                continue
            
            if not flag:
                break

        for i in range(b-idx, b+idx-1):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0

if N > 20:
    ans = [switch[i:i+20] for i in range(0, N, 20)]
    for i in ans:
        print(" ".join(map(str, i)))
else:
    print(" ".join(map(str, switch)))
