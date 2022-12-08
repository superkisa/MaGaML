def DPKnapsackItems(W, N, omega, c):
    d = [[0] * (W + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if omega[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w],
                              d[i - 1][w - omega[i - 1]] + c[i - 1])
    items = []
    for i in range(N, 0, -1):
        if d[i][W] != d[i - 1][W]:
            items.append(i)
            W -= omega[i - 1]
    print(d[-1][-1], len(items), sep='\n')
    print(*items[::-1])


W, N = list(map(int, input().split()))
omega = list(map(int, input().split()))
c = list(map(int, input().split()))

DPKnapsackItems(W, N, omega, c)
