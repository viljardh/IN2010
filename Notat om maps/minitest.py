import analprobing

d = analprobing.LinearProbing()

d['a'] = 0
print(d)
d['b'] = 1
print(d)
d['c'] = 2
print(d)
d['d'] = 3
print(d)
del d['a']
print(d)
del d['b']
print(d)
del d['c']
print(d)
del d['d']
print(d)
