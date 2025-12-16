#include "graphics.h"
#include <math.h>

int mask[] = {400, 300, 800, 600};

void masked_line(float x0, float y0, float x1, float y1) {
    float dx = x1 - x0, dy = y1 - y0;
    float steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    for (int i = 0; i <= steps; i++) {
        x0 += dx / steps;
        y0 += dy / steps;
        if (mask[0] < x0 && x0 < mask[2] && mask[1] < y0 && y0 < mask[3])
            continue;
        putpixel(x0, y0, RED);
    }
    glFlush();
}

void display() {
    rectangle(mask[0], mask[1], mask[2], mask[3]);
    masked_line(100, 100, 1000, 800);
    masked_line(100, 500, 1000, 500);
    masked_line(100, 800, 1000, 200);
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
