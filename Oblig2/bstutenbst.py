sortarr = [i for i in range(0, 11)]


def urgh(arr):
    if len(arr) > 1:
        i = len(arr)//2
        print(arr.pop(i))
        sl1 = arr[:i]
        sl2 = arr[i:]
        urgh(sl2)
        urgh(sl1)

    elif len(arr) == 1:
        print(arr.pop())


urgh(sortarr)
