#include <stdio.h>
#include <stdlib.h>
#define MAX 5

struct Node {
    int data;
    struct Node *next;
};

struct Node *head;

void push(int data) {
    struct Node *new;
    new = malloc(sizeof(struct Node));
    new->data = data;
    new->next = head;
    head = new;

    printf("new: %d\n", (*head).data);
    printf("under: %d\n", (*(*head).next).data);
}

void pop() {
    if ((*head).next == NULL) printf("underflow!\n");
    else head = (*head).next;
}

void display() {
    for (struct Node iter = *head; iter.next != NULL; iter = *iter.next) {
        printf("%d\n", iter.data);
    }
}

int main() {
    struct Node init;
    init.next = NULL;
    head = &init;

    int choice, data;

    printf("1: push; 2: pop; *: exit\n");

    while (1) {
        printf("\n > ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            scanf("%d", &data);
            push(data);
            break;
        case 2: pop(); break;
        default: return 0; break;
        }
        display();
    }
}
