#include "graphics.h"
#include <math.h>

void symmetry(int x, int y, int xc, int yc) {
    putpixel(xc + x, yc - y, RED); // For pixel (x,y)
    putpixel(xc + y, yc - x, RED); // For pixel (y,x)
    putpixel(xc + y, yc + x, RED); // For pixel (y,-x)
    putpixel(xc + x, yc + y, RED); // For pixel (x,-y)
    putpixel(xc - x, yc + y, RED); // For pixel (-x,-y)
    putpixel(xc - y, yc + x, RED); // For pixel (-y,-x)
    putpixel(xc - y, yc - x, RED); // For pixel (-y,x)
    putpixel(xc - x, yc - y, RED); // For pixel (-x,y)
}

void display() {
    int xc = getmaxx() / 2, yc = getmaxy() / 2, rad = 400;
    int x = 0;
    int y = rad;
    int p = 1 - rad;
    // symmetry(x, y, xc, yc);
    for (x = 0; y > x; x++) {
        if (p < 0) p += 2 * x + 3;
        else { p += 2 * (x - y--) + 5; }
        symmetry(x, y, xc, yc);
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
