from countswaps import CountSwaps


def sort(A):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    n = len(A)
    if n <= 1:
        return A
    i = (n + 1) // 2
    Ax = sort(A[:i])
    Ay = sort(A[i:])
    return merge(Ax, Ay, A)


def merge(Ax, Ay, A):
    i = 0
    j = 0
    nx = len(Ax)
    ny = len(Ay)

    while i < nx and j < ny:
        if Ax[i] < Ay[j]:
            A[i+j] = Ax[i]
            i += 1
        else:
            A[i+j] = Ay[j]
            j += 1

    while i < nx:
        A[i+j] = Ax[i]
        i += 1

    while j < ny:
        A[i+j] = Ay[j]
        j += 1

    return A