import sys

N = int(sys.stdin.readline())
coordinate = []
for i in range(N):
    x, y = (map(int, sys.stdin.readline().split()))
    coordinate.append([x, y])

coordinate = sorted(coordinate, key=lambda x: (x[0], x[1])) # x 값을 기준으로 오름차순 정렬

for j in range(0, len(coordinate)):
    print(coordinate[j][0], coordinate[j][1])

