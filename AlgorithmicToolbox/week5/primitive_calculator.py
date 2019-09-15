import sys

def optimal_sequence(n):
    a = [0] * (n+1)
    for i in range(1, len(a)):
        a[i] = a[i-1]+1
        if (i%2==0):
            a[i]=min(a[i//2]+1,a[i])
        elif (i%3==0):
            a[i]=min(a[i//3]+1,a[i])
    answer = []
    while(n>1):
        answer.append(n)
        
        if(n%2==0 and a[n] == a[n//2]+1):
            n//=2
        elif(n%3==0 and a[n] == a[n//3]+1):
            n//=3
        elif(a[n] == a[n-1]+1):
            n-=1
    answer.append(1)
    return reversed(answer)

if __name__=="__main__":
    n = sys.stdin.read()
    answer =list(optimal_sequence(int(n)))
    print(len(answer)-1)
    for i in answer:
        print(i, end=" ")
