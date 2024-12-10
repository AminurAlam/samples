#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int i, j;

void *thread_function() {
    printf("thread start\n");
    for (i = 0; i < 3; i++) {
        printf("%d\n", i);
        sleep(1);
    }
}

int main() {
    pthread_t a_thread;
    pthread_create(&a_thread, NULL, thread_function, NULL);
    pthread_join(a_thread, NULL);

    printf("main start\n");
    for (j = 20; j < 23; j++) {
        printf("%d\n", j);
        sleep(1);
    }
}
