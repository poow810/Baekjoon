import sys

string = sys.stdin.readline().strip()

dic = {
    "1" : 1, "2" : 1, "3" : 1, "4" : 1,
    "5" : 1, "6" : 2, "7" : 1, "8" : 1, "9" : 2, "0" : 1
}

count = 1
idx = 0
for i in string:
    if dic[i] == 0:
        count += 1
        for j in range(0, 10):
            if j == 6 or j == 9:
                dic[str(j)] += 2
            else:
                dic[str(j)] += 1

    if dic[i] > 0:
        if i == '6':
            dic[i] -= 1
            dic['9'] -= 1
        elif i == '9':
            dic[i] -= 1
            dic['6'] -= 1
        else:
            dic[i] -= 1
    
print(count)    
    