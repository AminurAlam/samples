#include <fcntl.h>
#include <unistd.h>

int main() {
    int buf[50];
    int fd_in = open("in.txt", O_RDWR); // hello world
    lseek(fd_in, -6, SEEK_END); // "world"
    write(1, buf, read(fd_in, buf, 5));
    lseek(fd_in, -6, SEEK_CUR); // " "
    write(1, buf, read(fd_in, buf, 1));
    lseek(fd_in, 0, SEEK_SET); // "hello"
    write(1, buf, read(fd_in, buf, 5));
}
