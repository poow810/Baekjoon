list1 = []
for i in range(1, 10001):
    a = i
    for j in str(i):
        a+=int(j)
    list1.append(a)
    if i not in list1:
        print(i)
