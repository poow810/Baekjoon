import sys

while True:
    A = list(map(int, sys.stdin.readline().strip()))
    if A[0] == 0:
        break
    temp = []
    for i in range(len(A)-1 ,-1,-1):
        temp.append(A[i])
    if A == temp:
        print("yes")
    else:
        print("no")