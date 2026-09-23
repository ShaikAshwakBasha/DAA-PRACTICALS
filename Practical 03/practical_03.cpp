#include <iostream>
using namespace std;
void heapify(int a[], int n, int i){int largest=i,left=2*i+1,right=2*i+2;if(left<n&&a[left]>a[largest])largest=left;if(right<n&&a[right]>a[largest])largest=right;if(largest!=i){swap(a[i],a[largest]);heapify(a,n,largest);}}
void heapSort(int a[], int n){for(int i=n/2-1;i>=0;i--)heapify(a,n,i);for(int i=n-1;i>0;i--){swap(a[0],a[i]);heapify(a,i,0);}}
int main(){int a[]={12,11,13,5,6,7};int n=6;heapSort(a,n);for(int x:a)cout<<x<<" ";}
