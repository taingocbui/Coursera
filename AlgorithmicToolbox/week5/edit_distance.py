import sys

def EditDistance(A,B):
    n = len(A)
    m = len(B)
    D = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range (1, n+1):
        D[i][0] = i
    for j in range (1, m+1):
        D[0][j] = j
    for j in range(1, m+1):
        for i in range(1, n+1):
            if(A[i-1] == B[j-1]):
                D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1,D[i-1][j-1])
            else:
                D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1,D[i-1][j-1]+1)
    return D[n][m]


if __name__=="__main__":
    print(EditDistance(input(), input()))
