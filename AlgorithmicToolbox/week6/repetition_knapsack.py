import sys

def repetition_knapsack(W, values, weights):
    v = [0 for x in range(W+1)]
    for w in range(1, W+1):
        v[w] = 0
        for i in range(len(weights)):
            if weights[i] <= w:
                val = v[w-weights[i]] + values[i]
                if val > v[w]:
                    v[w] = val
    return v[W]

if __name__=="__main__":
    input = sys.stdin.read()
    n, *data = [int(x) for x in input.split()]
    W = data[0]
    values = data[1::2]
    weights = data[2::2]
    print(repetition_knapsack(W,values, weights))