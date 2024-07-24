from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

queue = deque(lst)
lst2 = [0] * N
robot = deque(lst2)
count = 0
step = 1
while True:


    # 1단계
    queue.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0

    # 2단계
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0:
            if queue[i+1] >= 1:
                queue[i+1] -= 1
                

                robot[i+1] = 1
                robot[i] = 0
    
    robot[-1] = 0
    if queue[0] != 0:
        robot[0] = 1
        queue[0] -= 1

    if queue.count(0) >= K:
        break
    robot[N-1] = 0

    step += 1

print(step)