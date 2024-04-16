def sortl(A):
    n = len(A)
    N = 1000000
    B = []
    for i in range(N):
        B.append([])
    for i in A:
        B[i].append(i)
    j = 0
    for k in B:
        if k != []:
            for l in k:
                A[j] = l
                j += 1

    return A


from collections import defaultdict as dd
from time import time
import merge, insertion
from random import randint


def sortd(A):
    n = len(A)
    B = dd(list)

    for i in A:
        B[i].append(i)
    j = 0
    for k in B:
        if B[k]:
            for l in B[k]:
                A[j] = l
                j += 1

    return A


def partisan(A, l, h):
    p = randint(0, len(A))
    A[p], A[h] = A[h], A[p]
    pivot = A[h]
    left = l
    right = h + 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right += 1
        if left < right:
            A[left], A[right] = A[right], A[left]
    A[left], A[h] = A[h], A[left]
    return left


def dicksort(A):
    d = max(A)
    for i in range(d-1, -1, -1):
        A = sortl(A)
    return A


file = open("Merge/inputs/nearly_sorted_1000000")
A = []
for line in file:
    A.append(int(line.strip().split()[0]))

start = time()
sortd(A)
print("Time bucket: ", time() - start)

start = time()
merge.sort(A)
print("Time merge: ", time() - start)

start = time()
insertion.sort(A)
print("Time insertion: ", time() - start)


#print(sortl(A))
