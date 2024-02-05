import sys
from collections import deque

def push_front(x):

    return queue.appendleft(x)


def push_back(x):

    return queue.append(x)


def pop_front():
    
    if queue:
        return queue.popleft()
    else:
        return -1
    
def pop_back():
    
    if queue:
        return queue.pop()
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
    if "push_front" in command:
        command, n = command.split(" ")
        push_front(int(n))
    elif "push_back" in command:
        command, n = command.split(" ")
        push_back(int(n))
    elif command == "pop_front":
        print(pop_front())
    elif command == "pop_back":
        print(pop_back())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())