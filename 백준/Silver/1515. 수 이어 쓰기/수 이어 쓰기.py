import sys
 
N = sys.stdin.readline().strip()

count = 0
idx = 0
while True:
    count += 1
    for i in str(count):
        if N[idx] == i:
            idx += 1
            if idx >= len(N):
                print(count)
                exit()