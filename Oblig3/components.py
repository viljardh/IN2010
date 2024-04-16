from EvenLessHappyLittleGraphs import mkgraph, mkactordict, mkmoviedict
from collections import defaultdict as dd
from time import time

adict = mkactordict("actors.tsv")
mdict = mkmoviedict("movies.tsv")
v, e, w = mkgraph(adict, mdict)


def dfs(avert, e, s):   # Enkel stack DFS som i tillegg tar
    visited = set()     # mengde skuespillernoder som argument
    stack = [s]
    result = []

    while stack:
        u = stack.pop()
        if u not in visited:
            result.append(u)
            visited.add(u)
            avert.remove(u)  # Og fjerner de når vi har besøkt
            for v in e[u]:
                stack.append(v)

    return result


compdict = dd(int)

start = time()
avert = set(v)
while avert:
    startnode = next(iter(avert))
    comp = dfs(avert, e, startnode)
    compdict[len(comp)] += 1
end = time()

keys = sorted(compdict.keys())[::-1]
print()
for i in keys:
    ant = compdict[i]
    if ant > 1:
        print("There are {} components of size {}".format(ant, i))
    else:
        print("There is {} component of size {}".format(ant, i))
print()
print("Time to find components: {:.2f}s".format(end - start))
