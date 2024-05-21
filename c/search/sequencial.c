#include <stdio.h>
#define MAX 5

int A[MAX] = {6, 3, 8, 16, 5};

int main() {
    int query;
    printf("enter query: ");
    scanf("%d", &query);

    for (int i = 0; i < MAX; i++) {
        if (A[i] == query) {
            printf("query found\n");
            return 0;
        }
    }

    printf("query not found\n");
    return 1;
}
