#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int A[5] = {1, 3, 2, 4, 5};

int main() {
    int key, i;
    for (int j = 2; j < 5; j++) {
        for (int i = 0; i < 5; i++) { printf("%d ", A[i]); }
        printf("\n");
        key = A[j];
        i = j - 1;
        while (i > 0 && A[i] > key) {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = key;
    }

    for (int i = 0; i < 5; i++) { printf("%d ", A[i]); }
    printf("\n");

    return 0;
}
