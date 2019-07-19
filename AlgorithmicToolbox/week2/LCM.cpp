//Task. Given two integers a and b, find their least common multiple.
//Input Format. The two integers a and b are given in the same line separated by space.
//Constraints. 1 ≤ a, b ≤ 2 · 10 9 .
//Output Format. Output the least common multiple of a and b.

#include <iostream>
#include <vector>
using namespace std;

int GCD(const long long a, const long long b){
    if(b==0)
        return a;
    return GCD(b, a%b);
}

long long LCM(const long long a, const long long b){
    return (a*b)/GCD(a, b);
}

int main(){
    vector<long long> list(2);
    for(int i=0; i<2; i++)
        cin>>list[i];
    long long answer = LCM(list[0], list[1]);
    cout<<answer<<"\n";

}