def bsearch_l(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


# x = sorted(x)
cin = []

with open("algo/input2.txt", "r") as i_f:
    for s in i_f.readlines():
        cin.append(list(map(int, s.rstrip("\n").split())))

x = [0] + cin[1]
x1 = cin[1]
x1.sort()
num = cin[0][1]
x.sort()
print(x)

res = [0]
i = 0

key = x[-1] // (num - 1)
while x[-1] - key > 0:
    res.append(bsearch_l(x[res[i]:], key))
    print(res[i])
    x = [i - key for i in x]
    print(res[i])
    i+=1
print(res)

for i in res[:-1]:
    print(x1[i])
