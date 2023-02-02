A = list()
for i in range(28):
    N = int(input())
    A.append(N)
    i+=1
for j in range(1,31):
    if j in A:
        continue
    else:
        print(j)
    j+=1
