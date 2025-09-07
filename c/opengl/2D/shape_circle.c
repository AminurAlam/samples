#include <GL/freeglut.h>
#include <GL/glut.h>
#include <math.h>

void display() {
    int radius = 300;
    glBegin(GL_LINES);
    glColor3f(0.2, 0.2, 0.2);
    glVertex2i(-780, 0);
    glVertex2i(780, 0);
    glVertex2i(0, -420);
    glVertex2i(0, 420);
    glEnd();
    glFlush();

    glColor3f(0, 1, 0);
    for (float i = 0; i < M_PI / 2; i += .001) {
        glBegin(GL_POINTS);
        glVertex2i(radius * -sin(i), radius * cos(i));
        glVertex2i(radius * sin(i), radius * -cos(i));
        glVertex2i(radius * sin(i), radius * cos(i));
        glVertex2i(radius * -sin(i), radius * -cos(i));
        glEnd();
        glFlush();
    }
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080 / 2);
    glutCreateWindow("graphics");
    gluOrtho2D(-780, 780, -420, 420);
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
