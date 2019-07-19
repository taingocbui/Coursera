//Task. Given an integer n, find the last digit of the nth Fibonacci number F n (that is, F n mod 10).
//Input Format. The input consists of a single integer n.
//Constraints. 0 ≤ n ≤ 10 7 .
//Output Format. Output the last digit of F n .

#include <iostream>
using namespace std;

int Pisano(const int m){
    int a = 0;
    int b = 1;
    int c;
    int i;
    for(i=0; i<m*m+1; i++){
        c = (a+b)%m;
        a = b;
        b = c;
        if(a==0 && b==1){
            break;
        }
    }
    return i+1;
}

long long Fibonacci(const int n){
    long long list[n+2];
    list[0] = 0;
    list[1] = 1;
    int i;
    for(i=2; i<=n; i++){
        list[i] = list[i-1] + list[i-2];
    }

    return list[n];
}

int main(){
    int n;
    cin>>n;
    int p = Pisano(10);
    int m = n%p;
    int ans = Fibonacci(m)%10;
    cout<<ans<<"\n";

}
