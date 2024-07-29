import sys

string = sys.stdin.readline().strip()
stack = []

answer = 0

for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        if string[i+1] == ')':
            stack.pop()
            answer += len(stack)

    elif string[i] == ')':
        if string[i-1] == ")":
            if stack:
                stack.pop()
                answer += 1

print(answer)