from itertools import permutations

def check(number):
    
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) +1):
        if number % i == 0:
            return False
    
    return True

def solution(numbers):
    
    numbers = list(numbers)
    lst = []
        
    for i in range(1, len(numbers) + 1):
        lst += (list(permutations(numbers, i)))
    lst = set([int(''.join(i)) for i in lst])
    
    ans = 0
    for i in lst:
        flag = check(i)
        if flag:
            ans += 1
    
    return ans