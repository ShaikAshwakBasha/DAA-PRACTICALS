#include <iostream>
using namespace std;
int linearSearch(int a[], int n, int key) { for (int i=0;i<n;i++) if(a[i]==key) return i; return -1; }
int binarySearch(int a[], int n, int key) {
    int low=0, high=n-1;
    while(low<=high){int mid=low+(high-low)/2; if(a[mid]==key) return mid; if(a[mid]<key) low=mid+1; else high=mid-1;}
    return -1;
}
int main(){
    int a1[]={10,25,7,40,15,30}; cout<<linearSearch(a1,6,40)<<endl;
    int a2[]={5,10,15,20,25,30,35,40}; cout<<binarySearch(a2,8,30)<<endl;
}
