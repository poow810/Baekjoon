import sys

P = int(sys.stdin.readline())
for i in range(P):
    T, *lst = map(int, sys.stdin.readline().split())
    step = 0

    # 버블 정렬 이용하여 앞에꺼부터 하나씩 뒤에꺼랑 자리 바꿔주면 됨
    for j in range(len(lst)-1):
        for k in range(j+1, len(lst)):
            if lst[j] > lst[k]:
                lst[j], lst[k] = lst[k], lst[j]
                step += 1
    print(T, step)