from itertools import compress


cin = []
with open("algo/HW7/input.txt", "r") as i_f:
    for s in i_f.readlines():
        cin.append(tuple(map(int, s.rstrip("\n").split())))

V, E = cin[0]

G = tuple(set() for i in range(V))
for v, u in cin[1:]:
    G[v].add(u)
    G[u].add(v)


def dfs(G, visited, s):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack[-1]
        if not visited[v]:
            # v is visited first time
            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)
        else:
            # all neighbours of v were visited
            vertex_stack.pop()


# compute the number of connected components:
visited = [False] * len(G)
cachelist = []
n_components = 0
for i in range(len(G)):
    if not visited[i]:
        dfs(G, visited, i)
        cachelist.append(visited.copy())
        n_components += 1
print(n_components)
# print(cachelist)

for i, entry in enumerate(cachelist):
    if i == 0:
        res = list(compress(range(V), entry))
        print(len(res))
        print(*res)
    else:
        mp = map(lambda a, b: bool(a - b), entry, cachelist[i - 1])
        res = list(compress(range(V), mp))
        print(len(res))
        print(*res)
