T = int(input())
for x in range(0, T):
    R, S = input().split()      # 공백으로 두 문자 받기
    list = []
    for i in S:              # S 문자열을 돌면서
        list.append(i*int(R))   # R만큼 문자를 반복해서 리스트에 넣기

    print(''.join(list))  # 리스트를 문자열로 출력