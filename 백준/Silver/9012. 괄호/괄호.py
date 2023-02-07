def isStackFull():
    global Size, top, stack
    if top >= Size - 1:
        return True
    else:
        return False


def push(data):
    global top, Size, stack, count
    top += 1
    stack[top] = data


def pop():
    global top, Size, stack
    data = stack[top]
    stack[top] = None
    top -= 1

    return data


def printResult(T):
    global result
    for i in range(T):
        print(result[i])


result = []
Size = 50
top = -1
count = 0
stack = [None for _ in range(Size)]

if __name__ == "__main__":

    T = int(input())
    for i in range(T):
        string = input()
        for j in string:
            push(j)
        while True:
            data = pop()
            if (count < 0):
                break
            if (data == ")"):
                count = count + 1
            elif (data == "("):
                count = count - 1
            elif (data == None):
                break

        if (count == 0):
            result.append("YES")
        else:
            result.append("NO")
        count = 0
        top = -1
    printResult(T)