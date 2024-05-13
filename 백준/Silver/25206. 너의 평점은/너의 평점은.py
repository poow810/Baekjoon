import sys


add = 0
subAdd = 0
for _ in range(20):
    string = sys.stdin.readline().rstrip()
    lst = string.split(' ')
    if lst[2] == 'A+':
        subAdd += (float(lst[1])*4.5)
        add += float(lst[1])
    elif lst[2] == 'A0':
        subAdd += (float(lst[1])*4.0)
        add += float(lst[1])
    elif lst[2] == 'B+':
        subAdd += (float(lst[1])*3.5)
        add += float(lst[1])
    elif lst[2] == 'B0':
        subAdd += (float(lst[1])*3.0)
        add += float(lst[1])
    elif lst[2] == 'C+':
        subAdd += (float(lst[1])*2.5)
        add += float(lst[1])
    elif lst[2] == 'C0':
        subAdd += (float(lst[1])*2.0)
        add += float(lst[1])
    elif lst[2] == 'D+':
        subAdd += (float(lst[1])*1.5)
        add += float(lst[1])
    elif lst[2] == 'D0':
        subAdd += (float(lst[1])*1.0)
        add += float(lst[1])
    elif lst[2] == 'F':
        add += float(lst[1])

if subAdd == 0:
    print('0.000000')
else:
    print(round(subAdd / add, 6))