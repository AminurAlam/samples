#include "graphics.h"

void display() {
    float x0 = 100, y0 = 100;
    float dx = 1800 - x0, dy = 900 - y0;

    int steps = std::max(abs(dx), abs(dy));

    for (int i = 0; i <= steps; i++) {
        putpixel(x0, y0, RED);
        x0 += dx / steps;
        y0 += dy / steps;
    }
    glFlush();
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
