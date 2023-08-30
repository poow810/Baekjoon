import sys

T = int(sys.stdin.readline())

for i in range(T):
    count = 0
    sum = 0 
    quiz = list(sys.stdin.readline())
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)