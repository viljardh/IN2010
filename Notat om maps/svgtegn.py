from hashing import *
import svgwrite
from svgwrite.shapes import Circle

def draw_distribution(dist, N):
    s = int(N**0.5)
    r = 0.5
    svg = svgwrite.Drawing(size=(s, s))
    svg.viewbox(0, 0, s, s)
    m = dist.most_common(1)[0][1]
    for y in range(s):
        for x in range(s):
            k = x + y * s
            opacity = dist[k]/m
            svg.add(Circle((x + r, y + r), r,
                           fill = 'purple',
                           fill_opacity = opacity))
    return svg

def drawhashfunctions(Ns, hashfunctions, strings):
    for N in Ns:
        for hashfn in hashfunctions:
            name = hashfn.__name__ + '_' + str(N) + '.svg'
            dist = hash_dist(hashfn, N, strings)
            svg = draw_distribution(dist, N)
            svg.saveas(name)

drawhashfunctions([4096],
                  [hash_string_bad, hash_string_alright, hash_string_good],
                  words)

