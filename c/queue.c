#include <stdio.h>
#define MAX 5

int A[MAX], f = -1, r = -1;

void display() {
    if (f == -1) {
        printf("[ ]\n");
        return;
    }

    printf("[ ");
    for (int i = f; i < r; i++) { printf("\033[33m%d\033[0m, ", A[i]); }
    printf("\033[33m%d\033[0m ]\n", A[r]);
}

void insert() {
    int item;
    if (r == MAX - 1) {
        printf("overflow!\n");
    } else {
        printf("insert: ");
        scanf("%d", &item);
        A[++r] = item;
        if (f == -1) f++;
    }
}

void delete() {
    if (f == -1) {
        printf("underflow!\n");
    } else if (r == f++) {
        printf("removed: %d\n", A[f - 1]);
        printf("reset queue!\n");
        f = -1;
        r = -1;
    } else {
        printf("removed: %d\n", A[f - 1]);
    }
}

int main() {
    int choice;

    printf("initialized array of size %d\n", MAX);
    printf("1: insert; 2: delete; 3: reset; 4: debug; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1: insert(); break;
        case 2: delete(); break;
        case 3: f = -1; r = -1; break;
        case 4: printf("front: %d; back: %d\n", f, r); break;
        default: return 0; break;
        }
        display();
    }
}
