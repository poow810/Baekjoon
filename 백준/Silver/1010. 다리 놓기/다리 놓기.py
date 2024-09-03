import sys
import operator as op
from functools import reduce

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

T = int(sys.stdin.readline().strip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(nCr(m, n))