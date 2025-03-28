from collections import defaultdict

def transport(mp, start, end, start_time, idx, danger_set):
    x, y = start
    t = start_time
    key = (x, y, t)
    if key in mp and idx not in mp[key]:
        danger_set.add(key)
    mp[key].add(idx)

    while (x, y) != (end[0], end[1]):
        t += 1
        if x != end[0]:
            x += 1 if x < end[0] else -1
        else:
            y += 1 if y < end[1] else -1
        key = (x, y, t)
        if key in mp and idx not in mp[key]:
            danger_set.add(key)
        mp[key].add(idx)

    return t

def solution(points, routes):
    mp = defaultdict(set)      
    danger_set = set()       

    for idx, route in enumerate(routes):
        t = 0
        for j in range(len(route) - 1):
            start = points[route[j] - 1]
            end = points[route[j + 1] - 1]
            t = transport(mp, start, end, t, idx, danger_set)

    return len(danger_set)

