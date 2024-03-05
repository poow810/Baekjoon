import sys

N = int(sys.stdin.readline())
check = []
for _ in range(N):
    check.append(int(sys.stdin.readline()))

stack = []
idx = 0
num = 1
ans = []
res = []
while idx < N:
    if num == N+1:
        while stack:
            ans.append(stack.pop())
            res.append('-')
            if not stack:
                break    
        break

    if check[idx] == num:
        ans.append(num)
        idx += 1
        num += 1
        res.append('+')
        res.append('-')
    else:
        stack.append(num)
        num += 1
        res.append('+')

    if stack:
        while stack and stack[-1] == check[idx]:
            ans.append(stack.pop())
            idx += 1
            res.append('-')

if ans == check:
    for i in res:
        print(i)

else:
    print('NO')