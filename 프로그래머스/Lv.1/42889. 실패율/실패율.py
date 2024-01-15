def solution(N, stages):
    

    count = [0] * (N+2)
    for j in stages:
        count[j] += 1

    fails = {}
    total = len(stages)

    for i in range(1, N+1):
        if count[i] == 0:
            fails[i] = 0
        else:
            fails[i] = count[i] / total
            total -= count[i]

    result = sorted(fails, key=lambda x: fails[x], reverse=True)

    return result
