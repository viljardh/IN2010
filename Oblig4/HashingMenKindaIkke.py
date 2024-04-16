#from sepchain import SeparateChaining
#d = SeparateChaining()

from probin import LinearProbing
d = LinearProbing()

n = int(input())

for i in range(n):
    inp = input().split()
    if len(inp) == 1:
        print(d.storr())
    else:
        x = int(inp[1])
        if inp[0] == "contains":
            if d[x]:
                print("true")
            else:
                print("false")
        elif inp[0] == "insert":
            d[x] = str(x)
        elif inp[0] == "remove":
            del d[x]
