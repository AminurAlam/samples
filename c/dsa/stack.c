#include <stdio.h>
#define MAX 5

int A[MAX], n;

void insert(int item) {
    if (n == MAX) printf("overflow!\n");
    else A[n++] = item;
}

void delete() {
    if (n == 0) printf("underflow!\n");
    else n--;
}

int main() {
    int choice, item;

    printf("1: insert; 2: delete; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            scanf("%d", &item);
            insert(item);
            break;
        case 2: delete(); break;
        default: return 0; break;
        }
        for (int i = 0; i < n; i++) printf("%d, ", A[i]);
    }
}
