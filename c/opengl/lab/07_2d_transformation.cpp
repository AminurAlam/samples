#include "conio.h"
#include "graphics.h"
#include <math.h>
#include <stdio.h>

class Triangle {
  public:
    double x1, y1, x2, y2, x3, y3;

    Triangle(double x1, double y1, double x2, double y2, double x3, double y3) {
        this->x1 = x1;
        this->y1 = y1;
        this->x2 = x2;
        this->y2 = y2;
        this->x3 = x3;
        this->y3 = y3;
    }

    void draw() {
        // printf("(%f, %f, %f, %f, %f, %f)\n", x1, y1, x2, y2, x3, y3);
        cleardevice();
        drawgrid();
        line(x1, y1, x2, y2);
        line(x2, y2, x3, y3);
        line(x3, y3, x1, y1);
    }

    void mov(double xlen, double ylen) {
        x1 += xlen;
        x2 += xlen;
        x3 += xlen;
        y1 += ylen;
        y2 += ylen;
        y3 += ylen;
    }

    void scale(double factor) {
        double x = (x1 + x2 + x3) / 3.0, y = (y1 + y2 + y3) / 3.0;
        if (x1 > x) x1 += factor;
        if (x1 < x) x1 -= factor;
        if (x2 > x) x2 += factor;
        if (x2 < x) x2 -= factor;
        if (x3 > x) x3 += factor;
        if (x3 < x) x3 -= factor;
        if (y1 > y) y1 += factor;
        if (y1 < y) y1 -= factor;
        if (y2 > y) y2 += factor;
        if (y2 < y) y2 -= factor;
        if (y3 > y) y3 += factor;
        if (y3 < y) y3 -= factor;
    }

    void rotate(double angle) {
        double a = (angle * M_PI) / 180.0;
        double ca = cos(a), sa = sin(a);
        double x = (x1 + x2 + x3) / 3.0, y = (y1 + y2 + y3) / 3.0;

        // printf("(%f, %f)\n", ca, sa);

        double _x1 = x + ((x1 - x) * ca) - ((y1 - y) * sa);
        double _y1 = y + ((x1 - x) * sa) + ((y1 - y) * ca);
        double _x2 = x + ((x2 - x) * ca) - ((y2 - y) * sa);
        double _y2 = y + ((x2 - x) * sa) + ((y2 - y) * ca);
        double _x3 = x + ((x3 - x) * ca) - ((y3 - y) * sa);
        double _y3 = y + ((x3 - x) * sa) + ((y3 - y) * ca);

        x1 = _x1;
        y1 = _y1;
        x2 = _x2;
        y2 = _y2;
        x3 = _x3;
        y3 = _y3;
    }

    void refx() {
        double x = getmaxx();
        x1 = (x - x1);
        x2 = (x - x2);
        x3 = (x - x3);
    }

    void refy() {
        double y = getmaxy();
        y1 = (y - y1);
        y2 = (y - y2);
        y3 = (y - y3);
    }

    void sheer(double factor) { x1 += y1 * factor; }
};

void display() {
    Triangle t = Triangle(960, 470, 910, 570, 1010, 570);
    t.draw();
    while (1) {
        switch (getch()) {
        case 'h': t.mov(-10, 0); break;
        case 'j': t.mov(0, 10); break;
        case 'k': t.mov(0, -10); break;
        case 'l': t.mov(10, 0); break;
        case 'a': t.scale(10); break;
        case 's': t.scale(-10); break;
        case ',': t.rotate(-30); break;
        case '.': t.rotate(30); break;
        case '<': t.rotate(-30); break;
        case '>': t.rotate(30); break;
        case 'x': t.refx(); break;
        case 'y': t.refy(); break;
        case 'd': t.sheer(-0.1); break;
        case 'f': t.sheer(0.1); break;
        }
        t.draw();
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
