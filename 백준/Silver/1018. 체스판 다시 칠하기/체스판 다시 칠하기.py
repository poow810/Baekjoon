import sys 

N, M = map(int, sys.stdin.readline().split())
mp = []
for _ in range(N):
    mp.append(sys.stdin.readline().strip())

color = []
for j in range(N - 7):
    for k in range(M - 7):
        white = 0
        black = 0
        for i in range(j, j + 8):
            for z in range(k, k + 8):
                if (i + z) % 2 == 0:
                    if mp[i][z] != 'W':
                        white += 1
                    if mp[i][z] != 'B':
                        black += 1
                else:
                    if mp[i][z] != 'B':
                        white += 1
                    if mp[i][z] != 'W':
                        black += 1
        color.append(white)
        color.append(black)

print(min(color))

