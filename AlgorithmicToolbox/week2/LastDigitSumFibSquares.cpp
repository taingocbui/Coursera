//Task. Compute the last digit of F 0 2 + F 1 2 + · · · + F n 2 .
//Input Format. Integer n.
//Constraints. 0 ≤ n ≤ 10 18 .
//Output Format. The last digit of F 0 2 + F 1 2 + · · · + F n 2 .

#include <iostream>
#include <vector>
using namespace std;

int Pisano(const int m){
    int a=0;
    int b=1;
    int c,i;
    for(i=0; i<m*m+1; i++){
        c = (a+b)%m;
        a = b;
        b = c;
        if(a==0 && b==1)
            break;
    }
    return i+1;
}

long long Fibonacci(const int n){
    long long list[n+2];
    list[0] = 0;
    list[1] = 1;
    for(int i=2; i<=n; i++){
        list[i] = list[i-1] + list[i-2];
    }
    return list[n];
}

int main(){
    int n;
    cin>>n;
    int p = Pisano(10);
    int n1 = n%p;
    int n2 = (n-1)%p;
    int answer = (Fibonacci(n1)%10 * (Fibonacci(n1)%10 + Fibonacci(n2)%10))%10;
    cout<<answer<<"\n";

}