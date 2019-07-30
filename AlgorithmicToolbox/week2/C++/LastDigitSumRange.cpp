//Task. Given two non-negative integers m and n, where m ≤ n, find the last digit of the sum F m + F m+1 +
//· · · + F n .
//Input Format. The input consists of two non-negative integers m and n separated by a space.
//Constraints. 0 ≤ m ≤ n ≤ 10 18 .
//Output Format. Output the last digit of F m + F m+1 + · · · + F n .

#include <iostream>
#include <vector>
using namespace std;

int Pisano(const int m){
    int a = 0;
    int b = 1;
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

long long Fibonacci(const long long n){
    long long list[n+2];
    list[0] = 0;
    list[1] = 1;
    for(int i=2; i<=n; i++){
        list[i] = list[i-1] + list[i-2];
    }
    return list[n];
}

int main(){
    vector<int> list(2);
    for(int i=0; i<2; i++){
        cin>>list[i];
    }
    int p = Pisano(10);
    int m = (list[0]+1)%p;
    int n = (list[1]+2)%p;
    int answer = (Fibonacci(n)%10 - Fibonacci(m)%10 + 10)%10;
    cout<<answer<<"\n";
}