import sys

N, type = map(str, sys.stdin.readline().split())
dic = dict()
for i in range(int(N)):
    string = sys.stdin.readline().strip()
    if string not in dic:
        dic[string] = 1

if type == 'Y':
    print(len(dic))
elif type == 'F':
    print(len(dic)//2)
else:
    print(len(dic)//3)