import sys

N = int(sys.stdin.readline().strip())

count = 0
cat = 0

while N > 0:
    if count == 0:
        cat += 1
        N -= 1
    
    else:
        if N <= count:
            count += 1
            break

        else:
            N -= cat
            cat += cat

    count += 1

print(count)