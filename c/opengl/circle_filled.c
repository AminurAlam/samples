#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1, 0, 0);

    float radius = 0.6f;
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0, 0);
    for (float i = 0; i <= 2*M_PI; i+=0.001)
        glVertex2f(radius * cos(i), radius * sin(i));
    glEnd();
    glFlush();
}

main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920/2, 1920/2);
    glutCreateWindow("circle");
    glutDisplayFunc(display);
    glutMainLoop();
}
