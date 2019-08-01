# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    rate = [values[i]/weights[i] for i in range(len(weights))]
    for k in range(len(weights)):
        if(capacity == 0):
            return value
        m = max(rate)
        lst = [i for i,j in enumerate(rate) if j==m]
        for n in lst:
            if(weights[n]>0):
                a = min(weights[n], capacity)
                value = value+a*m 
                capacity = capacity - a
                weights[n] = weights[n] - a
                if(weights[n] == 0):
                    rate[n] = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))