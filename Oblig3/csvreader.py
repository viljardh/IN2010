from HappyLittleGraphs import mkGraph, mkactordict, mkmoviedict
from collections import defaultdict as dd, deque
from csv import writer, DictWriter, reader, DictReader
from time import time

adic = mkactordict("actors.tsv")
mdic = mkmoviedict("movies.tsv")
v, e, w = mkGraph(adic, mdic)

start = time()
with open("v.csv", "w", encoding="utf-8") as vfile:
    vwriter = writer(vfile)
    vwriter.writerow(v)
vfile.close()

with open("e.csv", "w", encoding="utf-8") as efile:
    ewriter = DictWriter(efile, e.keys())
    ewriter.writeheader()
    ewriter.writerow(e)
efile.close()


with open("w.csv", "w", encoding="utf-8") as wfile:
    wwriter = DictWriter(wfile, w.keys())
    wwriter.writeheader()
    wwriter.writerow(w)
wfile.close()

end = time()
print("Time to write: " , end-start)

start = time()
with open("v.csv", "r", encoding="utf-8") as vfile:
    vreader = reader(vfile)
    v2 = set(next(vreader))
vfile.close()

with open("e.csv", "r", encoding="utf-8") as efile:
    ereader = DictReader(efile)
    e2 = {str(key):eval(content) for key, content in next(ereader).items()}
efile.close()

with open("w.csv", "r", encoding="utf-8") as wfile:
    wreader = DictReader(wfile)
    w2 = {eval(key):eval(content) for key, content in next(wreader).items()}
wfile.close()

end = time()
print("Time to read: " , end-start)