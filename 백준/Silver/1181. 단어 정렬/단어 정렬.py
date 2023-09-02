import sys

N = int(sys.stdin.readline())

string_list = []
for i in range(N):
    string = sys.stdin.readline().strip()
    if string not in string_list:
        string_list.append(string)

string_list.sort(key=lambda x: (len(x),x))

for j in range(len(string_list)):
    print(string_list[j])