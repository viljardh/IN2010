from collections import defaultdict as dd


# Ordbøker til oppslag av navn/titler med id som nøkkel
def mkactordict(n):
    adict = {}
    file = open(n, "r", encoding="utf-8")
    for line in file:
        line = line.strip().split("\t")
        id = line[0]
        name = line[1]
        movies = line[2:]
        adict[id] = name, movies
    file.close()
    return adict


def mkmoviedict(n):
    mdict = {}
    file = open(n, "r", encoding="utf-8")
    for line in file:
        line = line.strip().split("\t")
        id = line[0]
        title = line[1]
        w = line[2]
        mdict[id] = title, w
    file.close()
    return mdict


def mkGraph(adict, mdict):
    # adict: aid : [name, [movies]]
    # mdict: mid : [title, rating]

    v = set()  # aid
    e = dd(set)  # aid : {aid, ..., aid}
    w = dd(list)  # (aid, aid) : [(title, rating), ..., (title, rating)]

    alist = adict.keys()
    for i in range(len(alist)):
        a = alist[i]
        for m in adict[a][1]:
            if m in mdict:  # Kun interessert i skuespillere fra filmer vi har data på
                v.add(a)
        for j in range(i, len(alist)):  # Går gjennom alle filmer en skuespiller har spilt i
            b = alist[j]
            for m in adict[b][1]:  # Og sammenligner. Har de spilt en film sammen
                if m in adict[a][1] and m in mdict:  # blir de lagt til, merket og vektet
                    try:  # Hvis vi ikke har data på filmen legges ikke kant til
                        e[a].add(b)  # Skuespiller har også spilt med seg selv
                        e[b].add(a)  # Set overser duplikater som er greit her
                        w[(a, b)].append((m, float(mdict[m][1])))
                        if a != b:   # Trenger ikke flere kanter på samme film på samme skuepsiller
                            w[(b, a)].append((m, float(mdict[m][1])))
                    except KeyError: # Hvis vi ikke har data på filmen hopper vi videre
                        continue

    return v, e, w

adict = mkactordict("data/marvel_actors.tsv")
mdict = mkmoviedict("data/marvel_movies.tsv")

v, e, w = mkGraph(adict, mdict)

for i in w:
    print(i, w[i])