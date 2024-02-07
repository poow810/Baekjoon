for t in range(10):
    N, string = map(str, input().split())
    stack = []

    for i in string:
        if not stack:
            stack.append(i)
        
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f"#{t+1}", "".join(stack))