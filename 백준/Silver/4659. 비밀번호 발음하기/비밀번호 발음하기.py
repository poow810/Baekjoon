import sys

a = ['a', 'e', 'i', 'o', 'u']

while True:
    string = sys.stdin.readline().strip()
    
    if string == 'end':
        break
    
    flag = True
    
    if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
        pre = ''
        count = 0
        for i in string:
            if pre == i:
                if pre+i == 'ee' or pre+i == 'oo':
                    continue
                else:
                    flag = False
            
            if pre in a and i in a:
                count += 1
            elif pre not in a and i not in a:
                count += 1
            elif pre in a and i not in a:
                count = 1
            elif pre not in a and i in a:
                count = 1

            if count == 3:
                flag = False
            
            pre = i

    else:
        flag = False

    if flag:
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')

