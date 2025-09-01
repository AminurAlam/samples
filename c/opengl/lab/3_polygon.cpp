#include <math.h>
#include "./graphics.h"

void display() {
    // drawgrid();

    int xc, yc = 540;
    // tri
    xc = 540;
    int len = 100;
    // int x1 = sin(xc+100)
    // int tri[] = {100,100, 100,500, 500,100};
    // drawpoly(3, tri);
    glBegin(GL_POINTS);
    for (float i = 0; i <= M_PI/2; i += M_PI/4) {
        glVertex2i(len * -sin(i) + xc, len * cos(i) + yc); // BL
        glVertex2i(len * sin(i) + xc, len * -cos(i) + yc); // TR
        glVertex2i(len * sin(i) + xc, len * cos(i) + yc); // BR
        glVertex2i(len * -sin(i) + xc, len * -cos(i) + yc); // TL
    }
    glEnd();
    glFlush();
    glBegin(GL_LINES);
    for (float i = 0; i <= M_PI/2; i += M_PI/4) {
        glVertex2i(len * -sin(i) + xc, len * cos(i) + yc); // BL
        glVertex2i(len * sin(i) + xc, len * -cos(i) + yc); // TR
        glVertex2i(len * sin(i) + xc, len * cos(i) + yc); // BR
        glVertex2i(len * -sin(i) + xc, len * -cos(i) + yc); // TL
    }
    glEnd();
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
