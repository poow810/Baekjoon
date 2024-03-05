import sys

def one(lst, N):

    add = 0
    for i in range(N):
        add += lst[i]
    
    return round(add / N)


def two(lst, N):

    return lst[N//2]

def three(lst, N):

    dic = {}
    for i in range(N):
        if lst[i] not in dic:
            dic[lst[i]] = 1
        else:
            dic[lst[i]] += 1
    
    max_value = 0
    for value in dic.values():
        if max_value < value:
            max_value = value

    c = 0
    for value in dic.values():
        if max_value == value:
            c += 1

    count = 0
    for key in dic.keys():
        if count == 1:
            if max_value == dic[key]:
                return key
            
        if max_value == dic[key]:
            count += 1
            if N == 1 or c == 1:
                return key


def four(lst):
    return lst[-1] - lst[0]


N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
print(one(lst, N))
print(two(lst, N))
print(three(lst, N))
print(four(lst))