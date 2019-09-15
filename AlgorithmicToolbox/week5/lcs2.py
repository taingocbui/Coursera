import sys

def LCS2(A,B):
    n = len(A)
    m = len(B)
    D = [[0 for x in range(m+1)] for y in range(n+1)]
    for j in range(1,m+1):
        for i in range(1, n+1):
            if(A[i-1] == B[j-1]):
                D[i][j] = D[i-1][j-1]+1
            else:
                D[i][j] = max(D[i-1][j],D[i][j-1])
    return D[n][m]

if __name__=="__main__":
    input = sys.stdin.read()
    data = [int(x) for x in input.split()]
    n = data[0]
    A = data[1:n+1]
    m = data[n+1]
    B = data[n+2:]
    print(LCS2(A,B))