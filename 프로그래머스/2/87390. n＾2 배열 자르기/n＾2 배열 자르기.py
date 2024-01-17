def solution(n, left, right):
    
    arr = []

    for i in range(left, right + 1):
        a, b = i // n, i % n
        if a > b :
            arr.append(a+1)
        else:
            arr.append(b+1)
    return arr
