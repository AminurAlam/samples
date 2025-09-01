#include "./graphics.h"

void display() {
    line(100, 540, 1800, 540); // horizontal line
    line(960, 100, 960, 1000); // vertical line
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
