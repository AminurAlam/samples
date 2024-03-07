#include <stdio.h>
#define MAX 10

int A[MAX], f = -1, r = -1;

void display() {
    if (f == -1) {
        printf("empty\n");
        return;
    }

    printf("[ ");
    for (int i = 0; i < r; i++) {
        printf("%d", A[i]);
        printf(", ");
    }
    printf("%d ]\n", A[r]);
}

void insert(int item) {
    if (r == MAX - 1) {
        printf("overflow!\n");
    } else {
        A[++r] = item;
        if (f == -1) f++;
    }
}

void delete() {
    if (f == -1) {
        printf("underflow\n");
    } else if (f == r--) {
        r = -1;
        f = -1;
    }
}

int main() {
    int item, choice;

    printf("choose:\n");
    printf("1 - insert\n");
    printf("2 - delete\n");
    printf("3 - exit\n");

    while (1) {
        printf(" > ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            scanf("%d", &item);
            insert(item);
            break;
        case 2: delete(); break;
        default: return 1; break;
        }
        display();
    }
}
