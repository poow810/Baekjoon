def changeBinary(lst):

    binary_lst = []
    for i in range(len(lst)):
        if lst[i] == '0':
            binary_lst.append(int(lst[:i] + '1' + lst[i + 1:], 2))
        elif lst[i] == '1':
            binary_lst.append(int(lst[:i] + '0' + lst[i + 1:], 2))
    return binary_lst


def solution():
    
    binary_lst = changeBinary(binary)
    for i in range(len(ternary)):
        for j in range(3):
            if ternary[i] != str(j):
                check = ternary[:i] + str(j) + ternary[i + 1:]
                if int(check, 3) in binary_lst:
                    return int(check, 3)


T = int(input())
for t in range(T):
    binary = input()
    ternary = input()
    ans = solution()
    print(f"#{t+1}", ans)