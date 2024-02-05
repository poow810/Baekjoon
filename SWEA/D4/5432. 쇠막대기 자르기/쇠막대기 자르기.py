T = int(input())
for t in range(T):
    lst = input()
    stack = []
    bar = 0

    for i in range(len(lst)):
        if lst[i] == "(":
            stack.append(lst[i])
            if lst[i+1] == ")":
                 stack.pop()
                 bar += len(stack)
        
        elif lst[i] == ")":
            if lst[i-1] == ")":
                if stack:
                    stack.pop()
                    bar += 1
    print(f"#{t+1}", bar)
