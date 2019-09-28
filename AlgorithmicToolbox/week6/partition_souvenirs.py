import sys

def partition(W, items):
    count = 0
    n = len(items)
    values = [[0 for x in range(n+1)] for y in range(W+1)]
    for w in range(1, W+1):
        for i in range(1, n+1):
            values[w][i] = values[w][i-1]
            if items[i-1] <= w:
                val = values[w-items[i-1]][i-1] + items[i-1]
                if values[w][i] < val:
                    values[w][i] = val
            if values[w][i] == W:
                count+=1
    if count < 3:
        return 0
    return 1

if __name__=="__main__":
    input = sys.stdin.read()
    n, *data = [int(x) for x in input.split()]
    if n<3:
        print(0)
    W = sum(data)
    if W%3 != 0:
        print(0)
    else:
        print(partition(W//3, data))