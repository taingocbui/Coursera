# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    i = k = l
    j = r
    while i<=j:
        if a[i] < x:
            a[i], a[k] = a[k], a[i]
            i+=1
            k+=1
        elif a[i] == x:
            i+=1
        else:
            a[i], a[j] = a[j], a[i]
            j-=1

    return [k, j]    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    #Use partition3
    indexes = partition3(a, l, r)
    randomized_quick_sort(a, l, indexes[0]-1)
    randomized_quick_sort(a, indexes[1]+1, r)
    #Use partition2
    #m = partition2(a, l, r)
    #randomized_quick_sort(a, l, m - 1)
    #randomized_quick_sort(a, m + 1, r)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
