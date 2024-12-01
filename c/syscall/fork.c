#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void) {
    printf("before\n");
    pid_t p = fork();

    if (p == 0) {
        printf("parent pid is %d\n", getpid());
    } else {
        printf("child pid is %d\n", getpid());
        printf("child ppid is %d\n", getppid());
    }

    return 0;
}
