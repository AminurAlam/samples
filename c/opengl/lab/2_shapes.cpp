#include "graphics.h"

void display() {
    // square
    int side = 300, left = 200, top = 400;
    rectangle(left, top, left + side, top + side);

    // circle
    circle(850, 550, 200);
    circle(850, 550, 199);

    // rectangle
    left = 1200, top = 400;
    rectangle(left, top, left+550, top+300);
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
