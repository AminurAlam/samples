#include <stdio.h>
#define MAX 5

int A[MAX], item, choice, f = -1, r = -1;

void insert() {
    if (r == MAX - 1) printf("overflow!\n");
    else {
        printf("insert: ");
        scanf("%d", &item);
        if (f == -1) f++;
        A[++r] = item;
    }
}

void delete() {
    if (f == -1) printf("underflow!\n");
    else if (r == f++) {
        printf("removed: %d\n", A[f - 1]);
        f = -1; r = -1;
    } else printf("removed: %d\n", A[f - 1]);
}

void main() {
    printf("1: insert; 2: delete; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1: insert(); break;
        case 2: delete(); break;
        default: return; break;
        }
    }
}
