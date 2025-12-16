#include "conio.h"
#include "graphics.h"
#include <chrono>
#include <math.h>
#include <stdio.h>
#include <thread>

class Cube {
  public:
    double l, t, r, b, w;

    Cube(double left, double top, double right, double bottom, double w) {
        this->l = left;
        this->t = top;
        this->r = right;
        this->b = bottom;
        this->w = w;
    }

    void draw() {
        cleardevice();
        // drawgrid();
        bar3d(l, t, r, b, w, 0);
        delay(1000);
    }

    void movx(double len) {
        l += len;
        r += len;
    }

    void movy(double len) {
        t += len;
        b += len;
    }

    void scale(double factor) {
        r += factor;
        t -= factor;
        w += factor;
    }

    void rotatebl() {
        double lo = l, to = t, ro = r, bo = b;
        l = lo;
        t = bo;
        r = lo + (bo - to);
        b = bo + (ro - lo);
    }

    void rotatetr() {
        double lo = l, to = t, ro = r, bo = b;
        r = ro;
        b = to;
        l = ro - (bo - to);
        t = to - (ro - lo);
    }
};

void display() {
    Cube t = Cube(600, 350, 800, 450, 50);

    t.draw();
    t.movx(-100);
    t.draw();
    t.movy(100);
    t.draw();
    t.movy(-100);
    t.draw();
    t.scale(20);
    t.draw();
    t.scale(20);
    t.draw();
    t.scale(-30);
    t.draw();
    t.rotatetr();
    t.draw();
    delay(500);
    t.rotatebl();
    t.draw();
    delay(500);
    t.rotatetr();
    t.draw();
    delay(500);
    t.rotatebl();
    t.draw();
    delay(500);

    /*
    while (1) {
        switch (getch()) {
        case 'h': t.movx(-40); break;
        case 'l': t.movx(40); break;
        case 'j': t.movy(40); break;
        case 'k': t.movy(-40); break;
        case 'a': t.scale(10); break;
        case 's': t.scale(-10); break;
        case ',': t.rotatebl(); break;
        case '.': t.rotatetr(); break;
        }
        t.draw();
    } */
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
