import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
check = 'IOI'+'OI'*(N-1)
idx = 0
count = 0
while idx < M:
    if string[idx] == 'O':
        idx += 1
        continue

    else:
        if check == string[idx:idx+3+2*(N-1)]:
            count += 1
            idx += 2
        else:
            idx += 1
print(count)