import sys

def solution(mush, sum):

    for i in mush:
        sum += i
        if sum >= 100:
            pre_sum = 100 - (sum - i)
            next_sum = abs(sum - 100)
            if pre_sum >= next_sum:
                return sum
            else:
                return sum - i


    return sum


sum = 0
mush = []
for i in range(10):
    N = int(sys.stdin.readline())
    mush.append(N)

result = solution(mush, sum)
print(result)