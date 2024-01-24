import heapq
import sys

N = int(sys.stdin.readline()) # 3
T = int(sys.stdin.readline()) # 9
vote = list(map(int, sys.stdin.readline().split())) # 2 1 4 3 5 6 7 2

count = []
photo = []

for i in range(T):
    if vote[i] in photo: # 사진이 이미 있다면
        for j in range(len(photo)):
            if vote[i] == photo[j]:
                count[j] += 1
    else:
        if len(photo) >= N:
            for j in range(N):
                if count[j] == min(count):
                    del photo[j]
                    del count[j]
                    break
        photo.append(vote[i])
        count.append(1)

photo.sort()
for i in photo:
    print(i, end=" ")

