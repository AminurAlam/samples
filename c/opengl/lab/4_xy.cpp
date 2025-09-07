#include "graphics.h"
#include <math.h>

void display() {
    int x = getmaxx(), y = getmaxy();
    line(x / 2, 0, x / 2, y);
    line(0, y / 2, x, y / 2);

    int pad = 100, min = (x < y) ? x : y;
    circle(x / 4, y / 4, min / 4 - pad);
    rectangle(x / 2 + pad, pad, x - pad, y / 2 - pad);
    // ellipse(x*3/4, y*3/4, 0,0, x/4-pad, y/4-pad);
    rectangle(
        x / 4 - min / 4 + pad, y * 3 / 4 - min / 4 + pad, x / 4 + min / 4 - pad,
        y * 3 / 4 + min / 4 - pad
    );
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
