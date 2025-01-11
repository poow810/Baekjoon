import sys

A, B = map(str, sys.stdin.readline().split())

if len(A) == len(B):
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1

    print(len(A) - count)

else:
    max_count = 0
    for i in range(len(B)):        
        count = 0
        if i + len(A) > len(B):
            break

        for j in range(len(A)):
            if i+j >= len(B):
                break

            if A[j] == B[j+i]:
                count += 1
        if count > max_count:
            max_count = count

    print(len(A) - max_count)
        
