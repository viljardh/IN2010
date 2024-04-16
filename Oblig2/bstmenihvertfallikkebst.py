import heapq as h

sortarr = [i for i in range(0, 11)]
h.heapify(sortarr)


def urgh(arr):
    if len(arr) > 1:
        i = len(arr)//2
        sl = []
        for j in range(i):
            h.heappush(sl, h.heappop(arr))
        print(h.heappop(arr))
        urgh(arr)
        urgh(sl)

    elif len(arr) == 1:
        print(h.heappop(arr))


urgh(sortarr)
