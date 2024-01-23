import sys

string = sys.stdin.readline().strip()
N = len(string)
spx = N // 10
m = N % 10
for i in range(spx):
    print(string[i*10:10*(i+1)])
print(string[N-m:])