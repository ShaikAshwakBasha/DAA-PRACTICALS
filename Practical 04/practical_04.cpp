#include <iostream>
using namespace std;
long long factorialIterative(int n){long long fact=1;for(int i=2;i<=n;i++)fact*=i;return fact;}
long long factorialRecursive(int n){if(n<=1)return 1;return n*factorialRecursive(n-1);}
int main(){int n=5;cout<<"Iterative: "<<factorialIterative(n)<<endl;cout<<"Recursive: "<<factorialRecursive(n)<<endl;}
