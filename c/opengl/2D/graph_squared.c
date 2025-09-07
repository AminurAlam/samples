#include <GL/freeglut.h>
#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_LINES);
    glColor3f(0.2, 0.2, 0.2);
    glVertex2f(-1, 0);
    glVertex2f(1, 0);
    glVertex2f(0, -1);
    glVertex2f(0, 1);
    glEnd();
    glFlush();

    glColor3f(1, 0, 0);
    glBegin(GL_POINTS);
    for (float x = -1.0; x < 1.0; x += 0.001) { glVertex2f(x, pow(x, 2)); }
    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080 / 2);
    glutCreateWindow("graphics");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
