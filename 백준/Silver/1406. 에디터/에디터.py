import sys

lst1 = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
lst2 = []

for _ in range(M):
    string = list(sys.stdin.readline().split())
    if string[0] == 'L':
        if lst1:
            lst2.append(lst1.pop())

    elif string[0] == 'D':
        if lst2:
            lst1.append(lst2.pop())

    elif string[0] == 'B':
        if lst1:
            lst1.pop()
    
    else:
        lst1.append(string[1])

lst1.extend(reversed(lst2))
print(''.join(lst1))