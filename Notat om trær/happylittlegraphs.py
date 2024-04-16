from collections import defaultdict as dd, deque
from heapq import heappush, heappop
import graphviz

def lagmegengraf(fnavn):
    file = open(fnavn, 'r')
    V = set()
    E = dd(set)
    w = {}

    for line in file:
        u, v, weight = line.strip().split()
        V.add(u)
        V.add(v)
        E[u].add(v)
        E[v].add(u)
        w[(u, v)] = int(weight)
        w[(v, u)] = int(weight)

    return V, E, w


G = lagmegengraf("graf")
def drawgraph(G):
    V, E, w = G
    dot = graphviz.Graph()
    seen_edges = set()

    for u in V:
        dot.node(u)

        for v in E[u]:
            if (v, u) in seen_edges:
                continue
            seen_edges.add((u, v))
            dot.edge(u, v, label=str(w[(u, v)]))

    dot.render('graph', format='svg')

drawgraph(G)
"""_, v, w = G
print(v['A'])"""

def DFS(graf, s, visited, res):
    _, E, _ = graf
    visited.add(s)
    res.append(s)
    for v in E[s]:
        if v not in visited:
            DFS(graf, v, visited, res)
    return res

def DFSstack(graf, s):
    _, E, _ = graf
    stack = [s]
    visited = set()
    res = []
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            res.append(u)
            for v in E[u]:
                stack.append(v)
    return res


def BFS(graf, s, visited, res):
    _, E, _ = graf
    queue = [s]
    while queue:
        u = queue.pop(-1)
        if u not in visited:
            visited.append(u)
            res.append(u)
            for v in E[u]:
                queue.append(v)
    return res

def bfshort(G, s):
    _, E, _ = G
    parents = {s: None}
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for v in E[u]:
            if v not in parents:
                parents[v] = u
                queue.append(v)
    return parents


def bfsbetween(G, s, t):
    parents = bfshort(G, s)
    v = t
    path = []

    if t not in parents:
        return path
    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]

def bfsallbetween(G, s):
    V,_,_ = G
    parents = bfshort(G, s)
    paths = []

    for v in V:
        path = []
        while v:
            path.append(v)
            v = parents[v]
        paths.append(path[::-1])
    return paths


# print(DFSstack(G, 'A'))
# print(BFS(G, 'A', [], []))
# print(bfsbetween(G, 'A', 'I'))
#a = (sorted(bfsallbetween(G, 'A')))


def dijkstra(G, s):

    _, E, w = G
    queue = [(0, s)]
    dist = dd(lambda: float('inf'))
    dist[s] = 0

    while queue:
        cost, u = heappop(queue)
        if cost != dist[u]:
            continue
        for v in E[u]:
            c = cost + w[(u, v)]
            if c < dist[v]:
                dist[v] = c
                heappush(queue, (c, v))

    return dist

"""
dist = dijkstra(G, 'A')
a = list(zip(*sorted(dist.items())))
for i in range(len(a[0])):
    print(a[0][i], a[1][i])
"""

def shortest_paths_from(G, s):
    _, E, w = G
    queue = [(0, s)]
    dist = dd(lambda: float('inf'))
    parents = {s: None}
    dist[s] = 0

    while queue:
        cost, u = heappop(queue)
        if cost != dist[u]:
            continue
        for v in E[u]:
            c = cost + w[(u, v)]
            if c < dist[v]:
                dist[v] = c
                heappush(queue, (c, v))
                parents[v] = u

    return parents

#print(shortest_paths_from(G, 'A'))

def prim(G):
    V, E, w = G
    s = next(iter(V))
    queue = [(0, s, None)]
    parents = {}

    while queue:
        _, p, u = heappop(queue)
        if u not in parents:
            parents[u] = p
            for v in E[u]:
                heappush(queue, (w[(u, v)], v, u))
    return parents


def removenode(G, u):
    V, E, w = G
    Vn, En = V.copy(), E.copy()

    Vn.discard(u)
    del En[u]

    for v in Vn:
        nabo = En[v].copy()
        nabo.discard(u)
        En[v] = nabo

    return Vn, En, w


def biconnaive(G):
    V, E, w = G
    for v in V:
        Vn, _, _ = Gn = removenode(G, v)
        nodelist = DFSstack(Gn, next(iter(Vn)))
        if set(nodelist) != Vn:
            return False
        return True

#print(biconnaive(removenode(G, 'C')))

#print(biconnaive(G))

def sepvertrec(E, u, d, dybde, low, parent, seps):

    dybde[u] = low[u] = d

    for v in E[u]:
        if v in parent and parent[v] == u:
            continue
        if v in dybde:
            low[u] = min(low[u], dybde[v])
            continue
        parent[v] = u

        sepvertrec(E, v, d + 1, dybde, low, parent, seps)
        low[u] = min(low[u], low[v])
        if d <= low[v]:
            seps.add(u)


def sepvert(G):
    V, E, w = G
    s = next(iter(V))
    dybde = {s:0}
    low = {s:0}
    parent ={s:None}
    seps = set()

    for u in E[s]:
        if u not in dybde:
            parent[u] = s
            sepvertrec(E, u, 1, dybde, low, parent, seps)

    if len([u for u in E[s] if dybde[u] == 1]) > 1:
        seps.add(s)
    return seps


def isbicon(G):
    return len(sepvert(G)) == 0


def lagmegendag(fnavn):
    V = set()
    E = dd(set)

    for i in open(fnavn, 'r'):
        v, u = i.strip().split()
        V.add(v)
        V.add(u)
        E[v] = u

    return V, E


G = lagmegendag('grafigjen')

def reversermegengraf(G):
    En = dd(set)
    V, E = G
    for u in V:
        for v in E[u]:
            En[v].add(u)
    return V, En

def dfsvisit(G, u, visited, stack):
    V, E = G
    visited.add(u)
    for v in E[u]:
        if v not in visited:
            dfsvisit(G, v, visited, stack)
    stack.append(u)

def dfstopsort(G):
    V,E = G
    visited = set()
    stack = []
    for u in V:
        if u not in visited:
            dfsvisit(G, u, visited, stack)
    return stack

print(dfstopsort(G))