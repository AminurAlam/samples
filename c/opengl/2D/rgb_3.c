#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    float y, rgb, r = -1.0f, g = (float)2 / 3 - 1, b = (float)4 / 3 - 1;

    glBegin(GL_LINES);
    for (float rgb = 0; rgb < 1; rgb += (float)1 / 1080) {
        y = rgb * 2 - 1;

        glColor3f(rgb, 0, 0); glVertex2f(r, y); glVertex2f(1, y);
        glColor3f(0, rgb, 0); glVertex2f(g, y); glVertex2f(1, y);
        glColor3f(0, 0, rgb); glVertex2f(b, y); glVertex2f(1, y);
    }
    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080);
    glutCreateWindow("rgb3");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
