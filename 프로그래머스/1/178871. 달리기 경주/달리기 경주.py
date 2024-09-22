def solution(players, callings):
    name = {}
    count = {}
    for i in range(len(players)):
        name[players[i]] = i
        count[i] = players[i]

    for j in callings:
        rate = name[j]
        a = name[j]
        name[j] -= 1
        name[count[rate-1]] += 1
        b = a - 1

        count[a], count[b] = count[b], count[a]

    result = sorted(name, key=name.get)

    return result