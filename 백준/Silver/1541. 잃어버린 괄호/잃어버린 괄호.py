import sys


string = sys.stdin.readline().split("-")
lst = []

for i in string:
    sum = 0
    num = i.split("+")
    for j in num:
        sum += int(j)
    lst.append(sum)

ans = lst[0]

for z in range(1, len(lst)):
    ans -= lst[z]

print(ans)

