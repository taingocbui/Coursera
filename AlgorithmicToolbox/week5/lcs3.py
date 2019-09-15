import sys

def lcs3(A, B, C):
    a = len(A)
    b = len(B)
    c = len(C)
    D = [[[0 for x in range(c+1)] for y in range (b+1)] for z in range (a+1)]
    for k in range(1, c+1):
        for j in range(1, b+1):
            for i in range(1, a+1):
                if (A[i-1] == B[j-1] == C[k-1]):
                    D[i][j][k] = D[i-1][j-1][k-1]+1
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])
    return D[a][b][c]

if __name__=="__main__":
    input = sys.stdin.read()
    data = [int(x) for x in input.split()]
    a = data[0]
    A = data[1:a+1]
    b = data[a+1]
    B = data[a+2:a+2+b]
    c = data[a+2+b]
    C = data[a+3+b:]
    print(lcs3(A,B,C))
