import sys

lst = sys.stdin.readline().rstrip()
string = sys.stdin.readline().rstrip()

stack = []
n = len(string)

for i in range(len(lst)):
    stack.append(lst[i])
    if ''.join(stack[-n:]) == string:
        for j in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")

