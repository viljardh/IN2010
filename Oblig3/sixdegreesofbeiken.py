from EvenLessHappyLittleGraphs import mkactordict, mkmoviedict, mkgraph
from collections import deque
from time import time

adict = mkactordict("actors.tsv")
mdict = mkmoviedict("movies.tsv")

v, e, w = mkgraph(adict, mdict)
print()


def shortestpath(e, s):
    parents = {s: None}
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for v in e[u]:
            if v not in parents:
                parents[v] = u
                queue.append(v)
    return parents


def shortestpathbetween(e, a1, a2):
    parents = shortestpath(e, a1)
    v = a2
    path = []

    if a2 not in parents:
        return path

    while v:
        path.append(v)
        v = parents[v]

    return path[::-1]


def sixdegrees(a1, a2):
    start = time()
    path = shortestpathbetween(e, a1, a2)
    deg = len(path) - 1
    end = time()
    startname = adict[a1][0]
    endname = adict[a2][0]

    print("{:<20} {:<30} {:<6} {:<20}".format("Actor", "Movie", "Rating", "Actor"))
    for i in range(len(path)-1):
        a1 = path[i]
        a2 = path[i+1]
        a1name = adict[a1][0]
        a2name = adict[a2][0]
        mv = w[(a1, a2)][0][0]
        mvname = mdict[mv][0]
        mvrate = mdict[mv][1]
        print("{:<20} {:<30} {:<6} {:<20}".format(a1name, mvname, float(mvrate), a2name))
    print("There are {} degrees of separation between {} and {}".format(deg, startname, endname))
    print("It took {:.2f} seconds to complete the query".format(end - start))
    print()


sixdegrees("nm2255973", "nm0000460")
sixdegrees("nm0424060", "nm8076281")
sixdegrees("nm4689420", "nm0000365")
sixdegrees("nm0000288", "nm2143282")
sixdegrees("nm0637259", "nm0931324")
