import sys

def factorial(num):
    if num == 1:
        return 1
    if num == 0:
        return 1
    return num * factorial(num - 1)


N = int(sys.stdin.readline())
print(factorial(N))
