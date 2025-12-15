#include "graphics.h"
#include <math.h>

void display() {
    int offset = 100;
    int x = getmaxx() + offset, y = getmaxy() + offset;
    int ax = x / 4, ay = y / 4, bx = x * 3 / 4, by = y / 4, cx = x * 3 / 4,
        cy = y * 3 / 4, dx = x / 4, dy = y * 3 / 4;
    int roof_s = 120, roof_h = 200;
    int house_w = 200, house_s = 30;
    int door_w = 200, door_h = 300;

    int roof[] = {ax,          ay,          bx,          by,
                  bx - roof_s, by - roof_h, ax - roof_s, ay - roof_h};
    int front[] = {ax, ay, bx, by, cx, cy, dx, dy};
    int side[] = {ax,           ay,           ax - house_w, ay - house_s,
                  dx - house_w, dy - house_s, dx,           dy};
    int door[] = {
        x/2 - door_w/2, y*3/4,
        x/2 - door_w/2, y*3/4 - door_h,
        x/2 + door_w/2, y*3/4 - door_h,
        x/2 + door_w/2, y*3/4,
    };
    drawpoly(4, front);
    drawpoly(4, roof);
    drawpoly(4, side);
    drawpoly(4, door);
    line(ax - roof_s, ay - roof_h, ax - house_w, ay - house_s);
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
