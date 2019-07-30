# Uses python3
import sys


def pisano(m):
    a = 0
    b = 1
    ans = 0
    for i in range(0, m*m+1):
        c = (a+b)%m
        a = b
        b = c
        if(a==0 and b ==1):
            ans=i+1
            break
    return ans

def fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def get_fibonacci_huge(n, m):
    rem = n%pisano(m)
    return fibonacci(rem)%m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))