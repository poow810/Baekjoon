import sys


string = sys.stdin.readline().strip()
a = string.count('a')

string += string[0:a-1]
ans = 1e99
for i in range(len(string)-a+1):
    ans = min(ans, string[i:i+a].count('b'))

print(ans)