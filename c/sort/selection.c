#include <stdio.h>
#define MAX 10

int main() {
    int A[MAX] = {5, 2, 7, 12, 3, 9, 1, 3, 14, 6};
    int i, j, key, temp;

    for (i = 0; i < MAX - 1; i++) {
        key = i;
        for (j = i + 1; j < MAX; j++)
            if (A[j] < A[key]) key = j;

        temp = A[key];
        A[key] = A[i];
        A[i] = temp;
    }

    for (int k = 0; k < MAX; k++) printf("%d ", A[k]);

    return 0;
}
