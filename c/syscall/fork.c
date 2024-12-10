#include <stdio.h>
#include <unistd.h>

int main() {
    printf("before\n");
    pid_t p = fork();

    if (p == 0) {
        printf("clild pid is %d\n", getpid());
        printf("clild's parent pid is %d\n", getppid());
    } else {
        printf("parent pid is %d\n", getpid());
    }
}
