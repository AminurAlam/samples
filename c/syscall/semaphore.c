#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <semaphore.h>

int shared = 1;
sem_t s;

void *fun1() {
    sem_wait(&s);
    int x = shared;
    x++;
    sleep(1);
    shared = x;
    sem_post(&s);
}

void *fun2() {
    sem_wait(&s);
    int y = shared;
    y--;
    sleep(1);
    shared = y;
    sem_post(&s);
}

int main() {
    sem_init(&s, 0, 1);
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, fun1, NULL);
    pthread_create(&thread2, NULL, fun2, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    printf("Final value of shared is %d\n", shared);
}
