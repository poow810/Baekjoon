import sys


while True: 
    num = list(map(int,sys.stdin.readline().split()))
    num.sort()
    if num[0] == num[1] == num[2] == 0:
        break;
    
    diagonal = num[2]
    short = num[0]
    median = num[1]

    if diagonal**2 == (short**2)+(median**2):
        print("right")
    else:
        print("wrong")
