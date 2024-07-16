import sys

p, m = map(int, sys.stdin.readline().split())
ans = []
for _ in range(p):
    level, player = map(str, sys.stdin.readline().split())
    flag = False

    for room in ans:
        if len(room) < m and abs(int(level) - room[0][0]) <= 10:
            room.append((int(level), player))
            flag = True
            break

    if not flag:
        ans.append([(int(level), player)])

for j in ans:
    print("Started!" if len(j) == m else "Waiting!")
    j.sort(key=lambda x:x[-1])
    for lv, id in j:
        print(lv, id)