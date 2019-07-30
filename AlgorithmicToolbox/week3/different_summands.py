# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i=0
    while(n>0):
        i = i+1
        k = n-i
        if(i != k and k not in summands):
            n = k
            summands.append(i)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
        