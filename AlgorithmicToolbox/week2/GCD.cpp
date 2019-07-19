//Task. Given two integers a and b, find their greatest common divisor.
//Input Format. The two integers a, b are given in the same line separated by space.
//Constraints. 1 ≤ a, b ≤ 2 · 10 9 .
//Output Format. Output GCD(a, b).

#include <iostream>
#include <vector>
using namespace std;

int GCD(const int a, const int b){
    if(b==0)
        return a;
    return GCD(b, a%b);
}

int main(){
    vector<int> list(2);
    for(int i=0; i<2; i++)
        cin>>list[i];
    int answer = GCD(list[0], list[1]);
    cout<<answer<<"\n";
}   