# 각 노드의 부모를 구하는 방법
# 입력 받은 노드가 깊이 우선 탐색 순서 노드?
import sys


def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True

        # 하위 노드 탐색
        for j in graph[current]:
            if not visited[j]:  # 아직 방문하지 않았다면
                stack.append(j) # 그 값을 스택에 추가해주고
                idx[j] = current    # 부모 노드를 idx에 저장


N = int(sys.stdin.readline())
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(N-1):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1) # 서로 연결된 노드 인덱스에 해당 값을 넣어줌(간선 연결)

visited = [False]*(N+1)
idx = [0 for _ in range(N+1)] # 방문 시 부모 노드를 저장할 리스트
dfs(graph, 1, visited)
for k in range(2, N+1):
    print(idx[k])