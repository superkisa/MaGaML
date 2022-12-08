import math
import bisect


def lis(x):
    N = len(x)
    d = [math.inf] * (N + 2)
    d[0] = -math.inf
    for i in range(N):
        d[bisect.bisect_left(d, x[i])] = x[i]
    print(d)
    return bisect.bisect_left(d, math.inf) - 1


_ = input()
x = list(map(int, input().split()))
print(lis(x))
