import sys
sys.setrecursionlimit(10**6)


def dfs(N):
    com[N] += com[boss_list[N]]
    if tree:
        for j in range(len(tree[N])):
            dfs(tree[N][j])


n, m = map(int, sys.stdin.readline().split())
boss = list(map(int, sys.stdin.readline().split())) # 상사 번호 리스트
tree = [[] for _ in range(n+1)] # 트리
boss_list = [0 for _ in range(n+1)] # 직속 상사 번호
com = [0 for _ in range(n+1)] # 칭찬 횟수 리스트

# 트리 생성
for i in range(1, len(boss)):
    tree[boss[i]].append(i+1)
    boss_list[i+1] = boss[i]


for k in range(m):
    i, w = map(int, sys.stdin.readline().split())
    com[i] = com[i]+w


dfs(1)
com.pop(0)
print(*com)