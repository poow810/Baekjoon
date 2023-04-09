import sys


computer = int(sys.stdin.readline())
sequence = int(sys.stdin.readline())
matrix = [[] for _ in range(computer+1)]


for i in range(sequence):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = [False]*(computer+1)

def dfs(matrix, start, visited):
    count = 0
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True

        for j in matrix[current]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True
                count += 1
    return count

print(dfs(matrix, 1, visited))
