from collections import deque

def overhand():
    
    for i in range(N-int(N/3)):
        lst.append(lst.popleft())


def perfectShuffle(lst):

    n = len(lst)
    lst1 = []
    ans = []
    if n % 2 == 0:
        for i in range(N//2):
            ans.append(lst[i])
            ans.append(lst[i%(N//2)+N//2])
    else:
        for i in range(N//2):
            ans.append(lst[i])
            ans.append(lst[i%(N//2)+N//2+1])
        ans.append(lst[N//2])
    return ans


T = int(input())
for t in range(T):
    N, C = map(int, input().split())
    lst = deque(x for x in range(1, N+1))
    for _ in range(C):
        overhand()
        lst = deque(perfectShuffle(lst))
    print(f"#{t+1}", " ".join(map(str, lst)))