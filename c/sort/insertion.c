#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int A[5] = {99, 35, 44, 87, 11};

int main() {
    int i, j, key;

    int len, input;

    printf("enter array size: \n");
    scanf("%d", &len);

    for (i = 1; i < 5; i++) {
        key = A[i];
        for (j = i - 1; j >= 0 && key < A[j]; j--) {
            A[j + 1] = A[j];
        }
        A[j + 1] = key;
    }

    for (int k = 0; k < 5; k++) { printf("%d ", A[k]); }
    printf("\n");

    return 0;
}
