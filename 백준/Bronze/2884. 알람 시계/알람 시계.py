import sys

H, M = map(int, sys.stdin.readline().split())

if H == 0 and 0 <= M < 45:
    alert = 1440+M-45
    H = alert//60
    M = 60+M-45
    print(H, M)
else:
    alert = H * 60 + M - 45
    H = alert//60
    if M < 45:
        M = 60 + M - 45
    else:
        M = M-45
    print(H, M)

# 시간을 분으로 변경하고, 연산 후 분을 시간으로 바꾸기
# M = 0 ~ 44일 때만, H*60을 1440이라 지정