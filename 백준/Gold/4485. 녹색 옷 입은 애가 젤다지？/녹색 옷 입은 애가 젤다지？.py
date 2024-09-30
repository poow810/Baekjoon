import sys
from heapq import heappop, heappush

def is_valid(nx, ny):
		return 0 <= nx < N and 0 <= ny < N
		

def solution(x, y):
		
    hq = []
    heappush(hq, (mp[x][y], x, y))
    distance[x][y] = mp[x][y]
    
    while hq:
        cost, x, y = heappop(hq)
        
        if cost > distance[x][y]:
            continue
        
        distance[x][y] = cost

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if not is_valid(nx, ny):
                continue
                    
            next_dist = mp[nx][ny]
            new_dist = next_dist + cost
            
            if new_dist < distance[nx][ny]:
                distance[nx][ny] = new_dist
                heappush(hq, (new_dist, nx, ny))



count = 0
while True:
    count += 1
    N = int(sys.stdin.readline().strip())
    
    if N == 0:
        break

    mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    distance = [[int(1e99) for _ in range(N)] for _ in range(N)]
    solution(0, 0)

    print(f"Problem {count}: {distance[N-1][N-1]}")