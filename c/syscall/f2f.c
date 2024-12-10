#include <fcntl.h>
#include <unistd.h>

int main() {
    int buf[50];
    int fd_in = open("in.txt", O_RDWR);
    int fd_out = open("out.txt", O_RDWR);

    int size = read(fd_in, buf, 12);
    write(fd_out, buf, size);
}
