# Uses python3
import sys

def pisano(m):
    a = 0
    b = 1
    ans = 0
    for i in range (0, m*m+1):
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

def fibonacci_partial_sum_naive(from_, to):
    to = to+2
    from_ = from_+1
    p = pisano(10)
    to = fibonacci(to%p)%10
    from_ = fibonacci(from_%p)%10
    
    return (to+10 - from_)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))