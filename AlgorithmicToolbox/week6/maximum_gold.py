import sys

def non_rep_knapsack(W, data):
    n = len(data)
    value = [[0 for x in range(n+1)] for y in range(W+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            value[w][i] = value [w][i-1]
            if data[i-1] < w:
                val = value[w-data[i-1]][i-1] + data[i-1]
                if value[w][i] < val:
                    value[w][i] = val
    return value[W][n]



if __name__=="__main__":
    input = sys.stdin.read()
    W, *data = [int(x) for x in input.split()]
    n = data[0]
    data = data[1:]
    print(non_rep_knapsack(W, data))