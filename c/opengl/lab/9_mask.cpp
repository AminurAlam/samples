#include "graphics.h"
#include <math.h>

void display() {
    int mask[] = {400, 300, 800, 600};
    for (int x = 0; x < getmaxx(); x += 10) {
        for (int y = 0; y < getmaxy(); y += 10) {
            if (mask[0] < x && x < mask[2] && mask[1] < y && y < mask[3])
                continue;
            putpixel(x, y, RED);
        }
        glFlush();
    }
}

void keyboard(unsigned char key, int x, int y) {
    if (key == 'q') glutLeaveMainLoop();
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    int gd = DETECT, gm;
    initgraph(&gd, &gm);
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
