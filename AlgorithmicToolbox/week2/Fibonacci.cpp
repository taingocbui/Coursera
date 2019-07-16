//Problem Description
//Task. Given an integer n, find the nth Fibonacci number F n .
//Input Format. The input consists of a single integer n.
//Constraints. 0 ≤ n ≤ 45.
//Output Format. Output F n


#include <iostream>
using namespace std;

long long Fib(const int n){
	long long list[n+2];
	list[0] = 0;
	list[1] = 1;
	int i;
	for(i = 2; i <= n; i++){
		list[i] = list[i-1] + list[i-2];
	}

	return list[n];
}

int main(){
	int n;
	cin>> n;
	
	long long answer = Fib(n);
	cout<<answer<<"\n";
	
	return 0;
}
