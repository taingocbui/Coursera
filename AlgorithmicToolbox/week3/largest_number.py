#Uses python3

import sys

def compare_digit(a,b):
    A = str(a)+str(b)
    B = str(b)+str(a)
    return True if A>B else False

def largest_number(a):
    res = ""
    while(len(a)>0):
        max = a[0]
        for i in a[1:]:
            if(compare_digit(i,max)):
                max = i
        res += max
        a.remove(max)
    return res




if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    