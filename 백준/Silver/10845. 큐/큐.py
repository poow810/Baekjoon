import sys
from collections import deque

def push(x):

    return queue.append(x)


def pop():
    
    if queue:
        return queue.popleft()
    else:
        return -1
    

def size():

    return len(queue)


def empty():

    if queue:
        return 0
    else:
        return 1
    
def front():
    
    if queue:
        return queue[0]
    else:
        return -1
    
def back():

    if queue:
        return queue[-1]
    else:
        return -1


N = int(sys.stdin.readline())
queue = deque()
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
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())