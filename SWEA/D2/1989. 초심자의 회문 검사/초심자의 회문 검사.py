T = int(input())
for t in range(T):
    lst = list(input())

    def valid(lst):
        for i in range(len(lst)//2):
            if lst[i] == lst[len(lst)-i-1]:
                return 1
            return 0
        
    print(f"#{t+1}", valid(lst))
