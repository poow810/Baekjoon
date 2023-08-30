import sys

N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
max_score = max(score_list)

score = 0 
for i in score_list:
    i = i/max_score*100
    score += i

print((score)/N)

