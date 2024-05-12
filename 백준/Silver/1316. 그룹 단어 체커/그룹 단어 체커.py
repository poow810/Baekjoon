import sys

N = int(sys.stdin.readline().strip())
answer = N
for _ in range(N):
    string = sys.stdin.readline().strip()
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            continue

        elif string[i] in string[i+1:]:
            answer -= 1
            break

print(answer)