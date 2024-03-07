#include <stdio.h>

// + - * / %
void operate(int a[3][3], int b[3][3], char operation) {
    int SUM[3][3], MUL[3][3];
    printf("A %c B is:\n", operation);
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {

            // switch (operation) {
            // case '+': C[x][y] = a[x][y] + b[x][y]; break;
            // case '-': C[x][y] = a[x][y] - b[x][y]; break;
            // case '*': C[x][y] = a[x][y] * b[x][y]; break;
            // case '/': C[x][y] = a[x][y] / b[x][y]; break;
            // case '%': C[x][y] = a[x][y] % b[x][y]; break;
            // }
        }
    }
}

void cross(int a[3][3], int b[3][3]) {
    int C[3][3];
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) { C[x][y] = 1; }
    }
}

void fmt(int table[3][3]) {
    printf("[\n");
    for (int x = 0; x < 3; x++) {
        printf("  [");
        for (int y = 0; y < 3; y++)
            printf("%2d ", table[x][y]);
        printf("]\n");
    }
    printf("]\n");
}

int main() {
    int SUM[3][3], MUL[3][3],
    a[3][3] = { 1, 2, 3, 1, 2, 3, 1, 2, 3 },
    b[3][3] = { 3, 2, 1, 3, 2, 1, 3, 2, 1 };

    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {
            SUM[x][y] = a[x][y] + b[x][y];
            MUL[x][y] = a[x][y] * b[x][y];
        }
    }

    printf("A + B is:\n");
    fmt(SUM);
    printf("A * B is:\n");
    fmt(MUL);
}
