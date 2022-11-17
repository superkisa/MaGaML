# %%
def bsearch_l(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] > key:
            r = m
        else:
            l = m
    return r


cin = []

with open("algo/input2.txt", "r") as i_f:
    for s in i_f.readlines():
        cin.append(list(map(int, s.rstrip("\n").split())))

cin[1].sort()
x = cin[1].copy()
num = cin[0][1]
counter = num - 1
res = [0]
resu = [x[0]]

dist = (x[-1] - x[0]) // (num - 1)
for i in range(num - 1):
    if len(x[res[i]:]) >= counter:
        res.append(bsearch_l(x[res[i] + 1: - counter], dist) + res[i] + 1)
        resu.append(cin[1][res[i + 1]])
        counter -= 1
        x[res[i] + 2:] = [j - dist for j in x[res[i] + 2:]]
    else:
        resu += cin[1][len(cin[1]) - counter:]
        break
print(list(range(len(resu), 1, -1)))
diff = []
for i in range(len(resu) - 1, 0, -1):
    diff.append(resu[i] - resu[i - 1])
print(min(diff))
