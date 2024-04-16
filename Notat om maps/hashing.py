def hash_string_bad(s, N):
    return sum(ord(c) for c in s) % N


def hash_string_alright(s, N):
    return (31**len(s))*sum(ord(c) for c in s) % N


def hash_string_good(s, N):
    h = 0
    for c in s:
        h = 31 * h + ord(c)
    return h % N


with open('words', 'r') as f:
    words = [line.strip() for line in f]


from collections import Counter
def hash_dist(hashfn, N, strings):
    return Counter([hashfn(s, N) for s in strings])


"""
dist_bad = hash_dist(hash_string_bad, 7, words)
dist_alright = hash_dist(hash_string_alright, 7, words)
dist_good = hash_dist(hash_string_good, 7, words)
header = ['i', 'bad','alright', 'good']
rows = [[i, dist_bad[i], dist_alright[i], dist_good[i]] for i in range(7)]
print(header)
for i in rows:
    print (i)
"""
