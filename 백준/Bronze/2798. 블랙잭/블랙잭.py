def check_card(card, number):
    ans = 0
    for i in range(0, len(card)-2):
        for j in range(i+1, len(card)-1):
            for k in range(j+1, len(card)):
                sum = card[i] + card[j] + card[k]
                if number >= sum and ans < sum:
                    ans = sum
    return ans


N, M = map(int, input().split())
card_list = list(map(int, input().split()))
print(check_card(card_list, M))

