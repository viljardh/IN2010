from collections import defaultdict as dd


def lagettre():

    E = dd(set)
    cat = int(input())

    inp = list(map(int, input().split()))
    rot = inp[0]
    E[rot].update(inp[1:])

    inp = list(map(int, input().split()))
    while inp[0] != -1:
        E[inp[0]].update(inp[1:])
        inp = list(map(int, input().split()))

    return rot, E, cat


def finnvei(rot, E, cat):
    sti = [cat]
    while cat != rot:
        for i in E:
            if cat in E[i]:
                sti.append(i)
                cat = i

    return sti


rot, E, cat = lagettre()
vei = finnvei(rot, E, cat)

for i in vei:
    if i != rot:
        print(i, end=" ")
    else:
        print(rot)
