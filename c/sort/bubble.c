#include <stdio.h>
#define MAX 10

int main() {
    int A[MAX] = {5, 2, 7, 12, 3, 9, 1, 3, 14, 6};

    for (int i = 0; i < MAX - 1; i++) {
        for (int j = 0; j < MAX - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }

    for (int k = 0; k < MAX; k++) printf("%d ", A[k]);

    return 0;
}
