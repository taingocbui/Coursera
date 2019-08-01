# Uses python3
import sys

def get_change(m):
    answer = m//10
    answer = answer + (m%10)//5
    answer = answer + (m%10)%5
    return answer

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input())
    print(get_change(m))