#include <stdio.h>
#define MAX 7

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int A[], int low, int high) {
    int pivot = A[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (A[j] <= pivot) {
            i++;
            swap(&A[i], &A[j]);
        }
    }

    swap(&A[i + 1], &A[high]);
    return (i + 1);
}

void quick_sort(int A[], int low, int high) {
    if (low < high) {
        int mid = partition(A, low, high);
        quick_sort(A, low, mid - 1);
        quick_sort(A, mid + 1, high);
    }
}

int main() {
    int data[MAX] = {8, 7, 2, 1, 0, 9, 6};
    quick_sort(data, 0, MAX - 1);
}
