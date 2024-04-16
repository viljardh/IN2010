from collections import defaultdict as dd
from time import time

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
        w = float(line[2])
        mdict[id] = title, w, set()
    file.close()
    return mdict


def mkgraph(adict, mdict):
    start = time()

    v = dd(set)
    e = dd(set)
    w = dd(list)

    # Legger til skuespillere kun om vi har info på filmene de har spilt
    # og rensker slik at de bare har spilt i filmer vi har data på
    for i in adict:
        for j in adict[i][1]:
            if j in mdict:
                v[i].add(j)

    # Oppdaterer filmordboken sånn at filmen vet hvem som har spilt i den
    for i in v:
        for j in v[i]:
            mdict[j][2].add(i)

    # Går gjennom alle skuespillere i en film
    for mid in mdict:
        alist = list(mdict[mid][2])     # Liste over skuespillere i filmen
        for i in range(len(alist)):     # Sjekker alle skuespillerne etter seg
            for j in range(i, len(alist)):
                a1 = alist[i]
                a2 = alist[j]
                e[a1].add(a2)   # Legger til kanter
                e[a2].add(a1)   # og gir den en ID og vekt
                w[a1, a2].append((mid, mdict[mid][1]))
                if a1 != a2: # Trenger ikke to kanter på at skuespiller har spilt med seg selv
                    w[a2, a1].append((mid, mdict[mid][1]))
    end = time()
    print("Vertices: ", len(v))
    c = 0
    # Teller over alle kanter sånn at den inkluderer når de har spilt i flere filmer
    # og med seg selv
    for i in w:
        for j in w[i]:
            c += 1
    print("Edges: ", c)
    print("It took {:.2f} seconds to create the graph".format(end-start))

    return v, e, w


#adict = mkactordict("actors.tsv")
#mdict = mkmoviedict("movies.tsv")
#mkgraph(adict, mdict)
