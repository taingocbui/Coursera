# Uses python3
from sys import stdin

def pisano(m):
    a = 0
    b = 1
    for i in range(m*m+1):
        c = (a+b)%m
        a = b 
        b = c
        if(a==0 and b==1):
            ans = i+1
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

def fibonacci_sum_squares(n):
    p = pisano(10)
    n1 = fibonacci(n%p)%10
    n2 = fibonacci((n+1)%p)%10
    return (n1*n2)%10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
