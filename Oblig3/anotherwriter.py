from HappyLittleGraphs import mkGraph, mkactordict, mkmoviedict
from time import time

start = time()
adic = mkactordict("data/actors.tsv")
end = time()
print("adict time: ", end-start)

start = time()
mdic = mkmoviedict("data/movies.tsv")
end = time()
print("mdict time: ", end-start)

start = time()
v, e, w = mkGraph(adic, mdic)
end = time()
print("graph time: ", end-start)
print("Nodes: ", len(v))
c = 0
for i in e:
    for j in e[i]:
        c += 1
print("Vertices: ", c)

start = time()

vfile = open("graph/v_writefix.csv", "w", encoding="utf-8") # aid
for n in v:
    vfile.write(n + "\n")
vfile.close()


efile = open("graph/e_writefix.csv", "w", encoding="utf-8") # første kolonne aid, følgende er hvem de har spilt med
for k in e:
    efile.write(k + ",")
    for x in e[k]:
        efile.write(x + ",")
    efile.write("\n")
efile.close()

wfile = open("graph/w_writefix.csv", "w", encoding="utf-8") # første og andre kolonne er tuppel fulgt av film og vekt
for x in w:
    if len(w[x]) == 0: # Av en eller annen grunn blir det lagt til
        print("fant tom kant")
        continue       # tomme kanter, vil ikke ha noe av
    else:
        wfile.write(x[0] + "," + x[1] + ",")
        for y in w[x]:
            wfile.write(y[0] + "," + str(y[1]) + ",")
        wfile.write("\n")
wfile.close()
end = time()
print("Time to write: " , end-start)
