import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

A, B, C, D = 0, 0, 0, 0

status_a, status_b, status_c, status_d = 0, 0, 0, 0

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

for k in range(N):
    if string[k] == 'R':
        status_c = 1
    
    if string[k] == 'B' and status_c == 1:
        C += 1

for z in range(N):
    if string[z] == 'B':
        status_d = 1

    if string[z] == 'R' and status_d == 1:
        D += 1

print(min(A, B, C, D))
