from collections import deque

def solution(stones, k):
    min_max = float('inf')
    dq = deque()

    for i in range(len(stones)):
        # 현재 창 범위에서 벗어난 인덱스 제거
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # 새로운 원소가 기존보다 크면 기존 원소 제거 (최댓값 유지)
        while dq and stones[dq[-1]] < stones[i]:
            dq.pop()

        dq.append(i)

        # 창 크기가 k가 되었을 때부터 최댓값 후보 갱신
        if i >= k - 1:
            min_max = min(min_max, stones[dq[0]])

    return min_max
