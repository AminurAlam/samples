#include <stdio.h>
#define MAX 5

int A[MAX], n;

void push(int item) {
    if (n == MAX) printf("overflow!\n");
    else A[n++] = item;
}

void pop() {
    if (n == 0) printf("underflow!\n");
    else n--;
}

void display() {
    for (int i = 0; i < n; i++) printf("%d  ", A[i]);
}

int main() {
    int choice, item;

    printf("1: push; 2: pop; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            scanf("%d", &item);
            push(item);
            break;
        case 2: pop(); break;
        default: return 0; break;
        }
        display();
    }
}
