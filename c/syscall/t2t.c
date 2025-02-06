#include <unistd.h>

int main() {
    int buf[50];
    int size = read(0, buf, 50);
    write(1, buf, size);
}
