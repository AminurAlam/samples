#include <GL/freeglut.h>
#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 0.5f, 0.2f);
    glBegin(GL_TRIANGLES);
    GLfloat v1[] = {
        +0.5f, +0.5f, -0.0f,  // Top
        -0.5f, -0.5f, -0.0f, // Bottom-left
        +0.5f, -0.5f, -0.0f // Bottom-right
    };
    glVertex3fv(&v1[0]);
    glVertex3fv(&v1[3]);
    glVertex3fv(&v1[6]);
    GLfloat v2[] = {
        -0.5f, +0.5f, -0.0f,  // Top
        -0.5f, -0.5f, -0.0f, // Bottom-left
        +0.5f, -0.5f, -0.0f // Bottom-right
    };
    glVertex3fv(&v2[0]);
    glVertex3fv(&v2[3]);
    glVertex3fv(&v2[6]);
    glEnd();
    glFlush(); // or glFinish()
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
