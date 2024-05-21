#include <stdio.h>
#define MAX 5

int main() {
    int A[MAX] = {5, 2, 3, 9, 1};
    int i, j, key;

    for (i = 1; i < MAX; i++) {
        key = A[i];
        for (j = i - 1; j >= 0 && key < A[j]; j--) {
            A[j + 1] = A[j];
        }
        A[j + 1] = key;
    }

    for (int k = 0; k < MAX; k++) printf("%d ", A[k]);

    return 0;
}
