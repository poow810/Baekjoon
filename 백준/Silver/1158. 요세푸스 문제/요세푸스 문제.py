# 큐 구현
import sys

def dequeue():
    global front, rear
    i = 0
    while i <= N-1:
        i += 1
        front = front+K-1
        if front >= len(arr):
            front = front%len(arr)
        data_list.append(str(arr.pop(front)))
    return data_list


N, K = map(int, sys.stdin.readline().split())
arr = [x for x in range(1, N+1)]
front = rear = 0
data_list = []

print("<", ", ".join(dequeue()[:]),">", sep='')