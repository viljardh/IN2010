from EvenLessHappyLittleGraphs import mkactordict, mkmoviedict, mkgraph
from collections import defaultdict as dd
from time import time
from heapq import heappush, heappop

adict = mkactordict("actors.tsv")
mdict = mkmoviedict("movies.tsv")

v, e, w = mkgraph(adict, mdict)
print()


# Denne trengs hvis skuespillerne har spilt i flere filmer sammen
# Så må vi finne den som var best
def indexofbestmoviebetweentheactors(u, v):
    hrating = 0
    edges = w[(u, v)]
    index = 0
    for i in range(len(edges)):
        rating = edges[i][1]
        if rating > hrating:
            hrating = rating
            index = i
    return index


def dijkstraish(e, w, s):
    queue = [(0, s)]
    dist = dd(lambda: float("inf"))
    parents = {s : None}
    dist[s] = 0.0

    while queue:
        cost, u = heappop(queue)
        if cost != dist[u]:
            continue
        for v in e[u]:
            movie = w[(u, v)]
            mindex = indexofbestmoviebetweentheactors(u, v)
            c = cost + 10.0 - movie[mindex][1]
            if c < dist[v]:
                dist[v] = c
                heappush(queue, (c, v))
                parents[v] = u

    return parents  # startnodens distanse til andre noder


def chillestpathbetween(e, w, a1, a2):
    idksomething = dijkstraish(e, w, a1)
    v = a2
    path = []

    if a2 not in idksomething:
        return path

    while v:
        path.append(v)
        v = idksomething[v]

    return path[::-1]


def sixdegreesofdisneyplusandthrust(a1, a2):
    start = time()
    path = chillestpathbetween(e, w, a1, a2)
    end = time()
    weight = 0
    print("{:<20} {:<30} {:<6} {:<20}".format("Actor", "Movie played in", "Rating", "Actor"))
    for i in range(len(path)-1):
        a1 = path[i]
        a2 = path[i+1]
        a1name = adict[a1][0]
        a2name = adict[a2][0]
        mindex = indexofbestmoviebetweentheactors(a1, a2)
        mv = w[(a1, a2)][mindex][0]
        mvname = mdict[mv][0]
        mvrate = mdict[mv][1]
        weight += 10 - float(mvrate)
        print("{:<20} {:<30} {:<6} {:<20}".format(a1name, mvname, mvrate, a2name))

    print("Weight: {:.1f}".format(weight))
    print("It took {:.2f} seconds to complete the query".format(end - start))
    print()


sixdegreesofdisneyplusandthrust("nm2255973", "nm0000460")
sixdegreesofdisneyplusandthrust("nm0424060", "nm8076281")
sixdegreesofdisneyplusandthrust("nm4689420", "nm0000365")
sixdegreesofdisneyplusandthrust("nm0000288", "nm2143282")
sixdegreesofdisneyplusandthrust("nm0637259", "nm0931324")
