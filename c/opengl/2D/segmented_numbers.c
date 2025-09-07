#include <GL/freeglut.h>
#include <GL/glut.h>

// TODO: read from user input
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 0.0f, 0.0f);
    int count = 10, val[10] = {95, 5, 118, 117, 45, 121, 123, 69, 127, 125};
    float width = (float)2 / count, height = width * 1.3, padding = 0.022,
          start, end;

    glBegin(GL_LINES);
    for (int n = 0; n < count; n++) {
        start = ((n * width) - 1) + padding;
        end = start + width - 2 * padding;

        if (64 & val[n]) {
            glVertex2f(start, height);
            glVertex2f(end, height);
        }
        if (32 & val[n]) {
            glVertex2f(start, height / 2);
            glVertex2f(end, height / 2);
        }
        if (16 & val[n]) {
            glVertex2f(start, 0.0);
            glVertex2f(end, 0.0);
        }
        if (8 & val[n]) {
            glVertex2f(start, height / 2);
            glVertex2f(start, height);
        }
        if (4 & val[n]) {
            glVertex2f(end, height / 2);
            glVertex2f(end, height);
        }
        if (2 & val[n]) {
            glVertex2f(start, 0.0);
            glVertex2f(start, height / 2);
        }
        if (1 & val[n]) {
            glVertex2f(end, 0.0);
            glVertex2f(end, height / 2);
        }
    }
    glEnd();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) { glutLeaveMainLoop(); }

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920 / 2, 1080);
    glutCreateWindow("graphics");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
