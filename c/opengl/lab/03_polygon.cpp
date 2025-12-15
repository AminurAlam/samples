#include "graphics.h"
#include <math.h>

void display() {
    // drawgrid();

    // triangle
    int top = 350;
    int tri[] = {top, top, top + top / 2, top * 2, top / 2, top * 2};
    drawpoly(3, tri);

    // square
    int side = 300;
    int sqx = 1920 / 2 - side / 2, sqy = 1080 / 2 - side / 2;
    int quad[] = {sqx,        sqy,        sqx + side, sqy,
                  sqx + side, sqy + side, sqx,        sqy + side};
    drawpoly(4, quad);

    // rectangle
    int rex = 1300, rey = 430, l = 400, b = 200;
    int rec[] = {rex, rey, rex + l, rey, rex + l, rey + b, rex, rey + b};
    drawpoly(4, rec);
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
