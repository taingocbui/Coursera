# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (right + left)//2

    l = get_majority_element(a, left, mid)
    r = get_majority_element(a, mid, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == l:
            lcount+=1
    if lcount > (right - left)/2:
        return l

    rcount = 0
    for i in range (left, right):
        if a[i] == r:
            rcount+=1
    if rcount > (right - left)/2:
        return r
        
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
