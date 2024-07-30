import sys

string = sys.stdin.readline().strip()
stack = []

ans = 0
count = 1

for i in range(len(string)):

    if string[i] == '(':
        stack.append(string[i])
        count *= 2
    
    elif string[i] == '[':
        stack.append(string[i])
        count *= 3
    
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        
        if string[i-1] == '(':
            ans += count
        stack.pop()
        count //= 2
    
    elif string[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break

        if string[i-1] == '[':
            ans += count
        stack.pop()
        count //= 3

if stack:
    print(0)
else:
    print(ans)