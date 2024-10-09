def solution(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    k = len(nums) // 2
    if len(dic) > k:
        return k
    else:
        return len(dic)