import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    string = sys.stdin.readline().strip()
    if len(string) > 3:
        lst = deque(list(map(int, string[1:-1].split(','))))
    elif len(string) == 3:
        lst = deque([int(string[1])])
    else:
        lst = deque()
    
    flag = False
    reverse_flag = True
    for i in p:
        if i == 'R':
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        else:
            if not lst:
                print('error')
                flag = True
                break
            else:
                if reverse_flag:
                    lst.popleft()
                else:
                    lst.pop()
    if not flag:
        if reverse_flag:
            print('[' + ','.join(map(str, lst)) + ']')
        else:
            print('[' + ','.join(map(str, reversed(lst))) + ']')