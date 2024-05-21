#include <stdio.h>
#define MAX 5

int A[MAX] = {3, 5, 8, 12, 16};

int main() {
    int query;
    printf("enter query: ");
    scanf("%d", &query);

    for (int i = 0; query < A[i]; i++) {
        if (query == A[i]) {
            printf("query found\n");
            return 0;
        }
    }

    printf("query not found\n");
    return 1;
}
