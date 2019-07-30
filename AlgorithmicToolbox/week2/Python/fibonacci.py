# Uses python3
def calc_fib(n):
    lst = [None]*1000
    lst[0] = 0
    lst[1] = 1
    for i in range(2, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]

n = int(input())
print(calc_fib(n))