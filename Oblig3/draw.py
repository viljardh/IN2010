from HappyLittleGraphs import mkGraph, mkactordict, mkmoviedict
import graphviz

adic = mkactordict("data/marvel_actors.tsv")
mdic = mkmoviedict("data/marvel_movies.tsv")

v, e, w = mkGraph(adic, mdic)

def drawgraph(V, E, w):
    dot = graphviz.Graph()
    seen_edges = set()

    for u in V:
        aname = adic[u][0]
        dot.node(aname)

        for v in E[u]:
            if (v, u) in seen_edges:
                continue
            seen_edges.add((u, v))
            mtitle = mdic[w[(u, v)][0][0]]
            dot.edge(adic[u][0], adic[v][0], label=str(mtitle))

    dot.render('graf', format='png')

drawgraph(v, e, w)