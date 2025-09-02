#include "./graphics.h"
#include <math.h>

void display() {
    // drawgrid();

    int top = 350;
    int tri[] = {top, top, top + top / 2, top * 2, top / 2, top * 2};
    drawpoly(3, tri);

    int side = 300;
    int sqx = 1920 / 2 - side / 2, sqy = 1080 / 2 - side / 2;
    int quad[] = {sqx,        sqy,        sqx + side, sqy,
                  sqx + side, sqy + side, sqx,        sqy + side};
    drawpoly(4, quad);

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
