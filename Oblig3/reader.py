from HappyLittleGraphs import mkGraph, mkactordict, mkmoviedict
from time import time
from collections import defaultdict as dd


def reader():
    start = time()
    vfile = open("graph/v.csv", "r", encoding="utf-8")
    v2 = set()
    for line in vfile:
        v2.add(line.strip())
    vfile.close()
    end = time()
    print("Time to read v: {:.2f}s".format(end - start))

    start = time()
    efile = open("graph/e.csv", "r", encoding="utf-8")
    e2 = dd(set)
    for line in efile:
        line = line.strip().split(",")
        k = line[0]
        for i in line[1:]:
            if i != "":
                e2[k].add(i)
    efile.close()
    end = time()
    print("Time to read e: {:.2f}s".format(end - start))

    start = time()
    wfile = open("graph/w.csv", "r", encoding="utf-8")
    w2 = dd(list)
    for line in wfile:
        line = line.strip().split(",")
        k = (line[0], line[1])
        c = 2
        while c < len(line[2:]):
            w2[k].append((line[c], float(line[c+1])))
            c = c+2
    wfile.close()
    end = time()
    print("Time to read w: {:.2f}s".format(end - start))

    return v2, e2, w2
