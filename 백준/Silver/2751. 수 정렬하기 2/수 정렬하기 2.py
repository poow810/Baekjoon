import sys

N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for j in range(len(num_list)):
    print(num_list[j], end="\n")
    