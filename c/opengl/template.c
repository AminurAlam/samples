#include <GL/freeglut.h>
#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_POINTS);
    glBegin(GL_LINES);

    glColor3f(0.2, 0.2, 0.2);

    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080 / 2);
    glutCreateWindow("template");
    // gluOrtho2D(-780, 780, -420, 420);
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
