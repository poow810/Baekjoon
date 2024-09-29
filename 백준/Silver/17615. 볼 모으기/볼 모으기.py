import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

A, B = 0, 0

status_a, status_b = 0, 0

for i in range(N-1, -1, -1):
    if string[i] == 'B':
        status_a = 1

    if string[i] == 'R' and status_a == 1:
        A += 1

for j in range(N-1, -1, -1):
    if string[j] == 'R':
        status_b = 1
    
    if string[j] == 'B' and status_b == 1:
        B += 1

print(min(A, B))