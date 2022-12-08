def IfHalfPossible(N, c):
    half_sum = sum(c) / 2
    half_sum_int = int(half_sum)
    if half_sum != half_sum_int:
        bool_ans = bool(0)
    else:
        d = [[1] + [0] * half_sum_int for i in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, half_sum_int + 1):
                if c[i - 1] > j:
                    d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j] or d[i - 1][j - c[i - 1]]
        bool_ans = bool(d[-1][-1])
    print("YES" if bool_ans else "NO")


N = int(input())
c = list(map(int, input().split()))

IfHalfPossible(N, c)
