#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) { swap(a[j], a[j + 1]); swapped = true; }
        }
        if (!swapped) break;
    }
}
void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) if (a[j] < a[minIndex]) minIndex = j;
        swap(a[i], a[minIndex]);
    }
}
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
        a[j + 1] = key;
    }
}
void mergeArray(int a[], int l, int m, int r) {
    vector<int> temp; int i=l,j=m+1;
    while(i<=m && j<=r) temp.push_back(a[i]<=a[j]?a[i++]:a[j++]);
    while(i<=m) temp.push_back(a[i++]); while(j<=r) temp.push_back(a[j++]);
    for(int k=0;k<(int)temp.size();k++) a[l+k]=temp[k];
}
void mergeSort(int a[], int l, int r) {
    if(l>=r) return; int m=l+(r-l)/2; mergeSort(a,l,m); mergeSort(a,m+1,r); mergeArray(a,l,m,r);
}
int partitionArray(int a[], int low, int high) {
    int pivot=a[high], i=low-1;
    for(int j=low;j<high;j++) if(a[j]<=pivot){i++;swap(a[i],a[j]);}
    swap(a[i+1],a[high]); return i+1;
}
void quickSort(int a[], int low, int high) {
    if(low<high){int p=partitionArray(a,low,high);quickSort(a,low,p-1);quickSort(a,p+1,high);}
}
void print(int a[], int n){for(int i=0;i<n;i++) cout<<a[i]<<" "; cout<<endl;}
int main(){
    int src[]={64,34,25,12,22,11,90,45,78,3}; int n=10;
    int a[10];
    copy(src,src+n,a); cout<<"Original array: "; print(a,n); bubbleSort(a,n); cout<<"Sorted array: "; print(a,n);
    copy(src,src+n,a); selectionSort(a,n); print(a,n);
    copy(src,src+n,a); insertionSort(a,n); print(a,n);
    copy(src,src+n,a); mergeSort(a,0,n-1); print(a,n);
    copy(src,src+n,a); quickSort(a,0,n-1); print(a,n);
}
