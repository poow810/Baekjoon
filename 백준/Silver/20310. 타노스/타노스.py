import sys

string = list(sys.stdin.readline().rstrip())

n = string.count('0')
m = string.count('1')

check_n = 0
for i in string:
    if check_n == m//2:
        break
    if i == '1':
        string.remove(i)
        check_n += 1

check_m = 0
string = string[::-1]
for j in string:
    if check_m == n//2:
        break
    if j == '0':
        string.remove(j)
        check_m += 1

for z in string[::-1]:
    print(z, end="")