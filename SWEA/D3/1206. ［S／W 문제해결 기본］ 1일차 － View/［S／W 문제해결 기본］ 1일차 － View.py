for t in range(10):
    N = int(input())
    bd = list(map(int, input().split()))
    
    add = 0
    for i in range(2, len(bd)-2):
        second_num = 0
        max_num = 0
        if bd[i] > bd[i-2] and bd[i] > bd[i-1] and bd[i] > bd[i+1] and bd[i] > bd[i+2]:
            for j in range(i-2, i+3):
                if bd[j] > max_num:
                    second_num = max_num
                    max_num = bd[j]
                elif second_num < bd[j] < max_num:
                    second_num = bd[j]
            
            add += max_num - second_num
          
    
    print(f"#{t+1}", add)