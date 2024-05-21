#include <stdio.h>
#define MAX 10

int main() {
    int A[MAX] = {1, 2, 3, 5, 7, 9, 11, 12, 15, 17};
    int a = 0, b = MAX, mid, query;

    printf("enter search query: ");
    scanf("%d", &query);

    while (a <= b) {
        mid = (a + b) / 2;

        if (query > A[mid]) a = mid + 1;
        else if (query < A[mid]) b = mid - 1;
        else {
            printf("found at %d\n", mid);
            return 0;
        }
    }

    printf("query not found\n");
    return 1;
}
