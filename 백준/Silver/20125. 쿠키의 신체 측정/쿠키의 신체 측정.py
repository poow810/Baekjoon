import sys

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def left_hand(x, y):
    count = 0
    while True:
        if mp[x][y] == '_':
            return count
        if mp[x][y] == '*':
            count += 1
            if is_valid(x, y-1):
                y -= 1
            else:
                return count
        

def right_hand(x, y):
    count = 0
    while True:
        if mp[x][y] == '_':
            return count
        if mp[x][y] == '*':
            count += 1
            if is_valid(x, y+1):
                y += 1
            else:
                return count

def hurry(x, y):
    count = 0
    while True:
        if mp[x][y] == '_':
            return count, x, y
        if mp[x][y] == '*':
            count += 1
            if is_valid(x+1, y):
                x += 1
            else:
                return count, x, y


def left_leg(x, y):
    count = 0
    while True:
        if mp[x][y] == '_':
            return count
        if mp[x][y] == '*':
            count += 1
            if is_valid(x+1, y):
                x += 1
            else:
                return count

            
            

def right_leg(x, y):
    count = 0
    while True:
        if mp[x][y] == '_':
            return count
        if mp[x][y] == '*':
            count += 1
            if is_valid(x+1, y):
                x += 1
            else:
                return count


N = int(sys.stdin.readline())
mp = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

head_x, head_y = 0, 0
flag = False
for i in range(N):
    for j in range(N):
        if mp[i][j] == '*':
            head_x, head_y = i, j
            flag = True
            break
    if flag:
        break

heart_x, heart_y = head_x + 1, head_y
hand_r, hand_l = 0, 0
leg_r, leg_l = 0, 0

hand_l = left_hand(heart_x, heart_y-1)
hand_r = right_hand(heart_x, heart_y+1)
hurry, x, y = hurry(heart_x+1, heart_y)
leg_l = left_leg(x, y-1)
leg_r = right_leg(x, y+1)

print(heart_x+1, heart_y+1)
print(hand_l, hand_r, hurry, leg_l, leg_r)