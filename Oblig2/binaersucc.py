from set import *

n = int(input())
binaerset = Set()

for i in range(n):
    inp = input().split()
    if len(inp) == 1:
        print(storr(binaerset))
    else:
        x = int(inp[1])
        if inp[0] == "contains":
            if get(binaerset, x) is None:
                print("false")
            else:
                print("true")
        elif inp[0] == "insert":
            insert(binaerset, x)
        elif inp[0] == "remove":
            remove(binaerset, x)
