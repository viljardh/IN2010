sortarr = [i for i in range(0, 11)]


def urgh(arr):
    if len(arr) > 1:
        i = len(arr)//2
        sl1 = arr[:i]
        sl2 = arr[i:]
        print(sl2.pop(0))
        urgh(sl2)
        print(sl1.pop())
        urgh(sl1)
    #elif len(arr) == 2:
    #    print(arr.pop())
    #    print(arr.pop())
    elif len(arr) == 1:
        print(arr.pop())

    else:
        return


urgh(sortarr)
