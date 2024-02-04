for t in range(10):
    dump = int(input())
    ground = list(map(int, input().split()))
    
    max_ground = 0
    min_ground = 0

    while dump > 0:
        for i in range(len(ground)):
            if ground[i] > ground[max_ground]:
                max_ground = i
            if ground[i] < ground[min_ground]:
                min_ground = i

        ground[max_ground] -= 1
        ground[min_ground] += 1
        dump -= 1
    
    ans_max = 0
    ans_min = 1000
    for j in ground:
        if j > ans_max:
            ans_max = j
        if j < ans_min:
            ans_min = j
    
    print(f"#{t+1}", ans_max - ans_min)