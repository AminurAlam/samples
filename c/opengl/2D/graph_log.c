#include <GL/freeglut.h>
#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_LINES);
    glColor3f(0.2, 0.2, 0.2);
    glVertex2i(-300, 0);
    glVertex2i(300, 0);
    glVertex2i(0, -30);
    glVertex2i(0, 30);
    glEnd();
    glFlush();

    glColor3f(1, 0, 0);
    glBegin(GL_POINTS);
    for (float x = 0; x < 300; x += .1) { glVertex2f(x, log(x)); }
    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080 / 2);
    glutCreateWindow("graphics");
    gluOrtho2D(-300, 300, -30, 30);
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
