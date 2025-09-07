#include <GL/freeglut.h>
#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_LINES);
    float r, g, b, x, X;

    for (float rgb = 0; rgb < 1; rgb += (float)1 / 19200) {
        x = rgb * 2 - 1;
        X = (rgb + (float)1 / 19200) * 2 - 1;

        glColor3f(1 - rgb, rgb, 0); glVertex2f(x, (float)6 / 3 - 1); glVertex2f(X, (float)5 / 3 - 1);
        glColor3f(1 - rgb, 0, rgb); glVertex2f(x, (float)5 / 3 - 1); glVertex2f(X, (float)4 / 3 - 1);
        glColor3f(rgb, 1 - rgb, 0); glVertex2f(x, (float)4 / 3 - 1); glVertex2f(X, (float)3 / 3 - 1);
        glColor3f(0, 1 - rgb, rgb); glVertex2f(x, (float)3 / 3 - 1); glVertex2f(X, (float)2 / 3 - 1);
        glColor3f(rgb, 0, 1 - rgb); glVertex2f(x, (float)2 / 3 - 1); glVertex2f(X, (float)1 / 3 - 1);
        glColor3f(0, rgb, 1 - rgb); glVertex2f(x, (float)1 / 3 - 1); glVertex2f(X, (float)0 / 3 - 1);
    }
    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920, 1080 / 2);
    glutCreateWindow("graphics");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
