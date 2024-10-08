def solution(numbers):
    ans = ""
    numbers.sort(key=lambda x : str(x)*3, reverse=True)
    
    for i in numbers:
        ans += str(i)
    
    return str(int(ans))
        