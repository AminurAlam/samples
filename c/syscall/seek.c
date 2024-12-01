#include <fcntl.h>
#include <unistd.h>

int main(void) {
    int size;
    int buf[50];
    int fd_in = open("in.txt", O_RDWR);

    // world
    lseek(fd_in, -6, SEEK_END);
    size = read(fd_in, buf, 5);
    write(1, buf, size);

    //
    lseek(fd_in, -6, SEEK_CUR);
    size = read(fd_in, buf, 1);
    write(1, buf, size);

    // hello
    lseek(fd_in, 0, SEEK_SET);
    size = read(fd_in, buf, 5);
    write(1, buf, size);

    // \n
    lseek(fd_in, 11, SEEK_SET);
    size = read(fd_in, buf, 1);
    write(1, buf, size);

    return 0;
}
