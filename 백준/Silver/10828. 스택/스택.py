import sys

def push(x):

    return stack.append(x)


def pop():
    
    if stack:
        return stack.pop()
    else:
        return -1
    

def size():

    return len(stack)


def empty():

    if stack:
        return 0
    else:
        return 1
    
def top():
    
    if stack:
        return stack[-1]
    else:
        return -1


N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if "push" in command:
        command, n = command.split(" ")
        push(int(n))
    elif command == "pop":
        print(pop())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "top":
        print(top())
