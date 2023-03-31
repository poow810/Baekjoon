def check(n):
    count = 0
    for i in range(n):
        word = input()
        stack = []
        for j in word:
            if len(stack) == 0:
                stack.append(j)
            else:
                if j == "A":
                    if stack[-1] == "B":
                        stack.append(j)
                    elif stack[-1] == "A":
                        stack.pop()
                elif j == "B":
                    if stack[-1] == "A":
                        stack.append(j)
                    elif stack[-1] == "B":
                        stack.pop()
        if len(stack) == 0:
            count += 1
    return count
        
N = int(input())
print(check(N))