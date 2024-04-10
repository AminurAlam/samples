#include <stdio.h>
#define MAX 10

int A[MAX], len;

void insert(int item, int index) {
    if (len == MAX) printf("overflow!\n");
    else if (len >= index) {
        for (int i = len; i >= index; i--) A[i + 1] = A[i];
        A[index] = item;
        len++;
    } else {
        A[len++] = item;
    }
}

void delete(int index) {
    if (len == 0) printf("underflow!\n");
    else {
        for (int i = index; i < len; i++) A[i] = A[i + 1];
        len--;
    }
}

int main() {
    int choice, item, at;
    printf("1: insert; 2: delete; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            printf("item, index: ");
            scanf("%d %d", &item, &at);
            insert(item, at);
            break;
        case 2:
            printf("delete at index: ");
            scanf("%d", &at);
            delete (at);
            break;
        default: return 0; break;
        }
        for (int i = 0; i < len; i++) printf("%d, ", A[i]);
    }
}
