import sys

check = ['a', 'e', 'i', 'o', 'u']


def solution(string):
    
    # 첫 번째 조건
    flag = False
    for i in string:
        if i in check:
            flag = True
    
    if not flag:
        return False

    # 두 번째 조건
    mo = False
    ja = False
    count = 0
    for i in string:
        if i in check:
            if mo:
                count += 1
                if count == 3:
                    return False
                continue
            else:
                count = 1
                mo = True
                ja = False
        elif i not in check:
            if ja:
                count += 1
                if count == 3:
                    return False
                continue
            else:
                count = 1
                ja = True
                mo = False

    # 세 번째 조건
    temp = ""
    for i in string:
        if temp == i:
            if temp == "e" or temp == "o":
                continue
            else:
                return False
        temp = i
    
    return True

while True:

    string = sys.stdin.readline().strip()

    if string == "end":
        break

    answer = solution(string)

    if answer:
        print(f"<{string}> is acceptable.")
    else:
        print(f"<{string}> is not acceptable.")
