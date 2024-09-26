def move(n, roads, oils):
    cost = roads[0]*oils[0]
    first_oil = oils[0]
    r = 0
    for i in range(1, n-1):
        if oils[i] < first_oil:
            cost = cost + oils[i]*roads[i]
            first_oil = oils[i]
        else:
            cost = cost + first_oil*roads[i]

    return cost

N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

print(move(N, road, oil))