import sys

def merge(a, b, left, ave, right):
    number_of_inversions = 0
    L = a[left:ave]
    R = a[ave:right]

    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            b[k] = L[i]
            i+=1
        else:
            b[k] = R[j]
            j+=1
            number_of_inversions+=1
        k+=1
    
    while i < len(L):
        b[k] = L[i]
        i+=1
        k+=1
        number_of_inversions+=1
    
    while j < len(R):
        b[k] = R[j]
        j+=1
        k+=1
    for i in range(left, right):
        a[i] = b[i]
    return number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left+right)//2
    number_of_inversions += get_number_of_inversions(a,b,left, ave)
    number_of_inversions += get_number_of_inversions(a,b, ave, right)
    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions

if __name__=="__main__":
    input = sys.stdin.read()
    n, *data = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(data, b, 0, len(data)))