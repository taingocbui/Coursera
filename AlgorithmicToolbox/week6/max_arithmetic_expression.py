import sys

def evaluate(a,b, op):
    if op == "+":
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        assert False


def MinAndMax(i,j, M, m, op):
    minvalue = float("inf")
    maxvalue = float("-inf")
    for k in range(i,j):
        a = evaluate(M[i][k], M[k+1][j], op[k])
        b = evaluate(M[i][k], m[k+1][j], op[k])
        c = evaluate(m[i][k], M[k+1][j], op[k])
        d = evaluate(m[i][k], m[k+1][j], op[k])
        minvalue = min(minvalue, a,b,c,d)
        maxvalue = max(maxvalue, a,b,c,d)
    return (minvalue, maxvalue)

def parentheses(data):
    digits = data[0::2]
    operations = data[1::2]
    n = len(digits)
    m = [[0 for x in range(n)]for y in range(n)]
    M = [[0 for x in range(n)]for y in range(n)]
    for i in range (n):
        m[i][i] = int(digits[i])
        M[i][i] = int(digits[i])
    for s in range(1, n):
        for i in range(0, n-s):
            j = i+s
            m[i][j], M[i][j] = MinAndMax(i,j,M,m, operations)
    return M[0][n-1]

if __name__=="__main__":
    print(parentheses(input()))