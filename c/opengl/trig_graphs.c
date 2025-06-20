#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_LINES);
    glColor3f(0.2, 0.2, 0.2);
    glVertex2i(-780,0); glVertex2i(780,0);
    glVertex2i(0,-420); glVertex2i(0,420);
    glEnd();

    glBegin(GL_POINTS);
    int radius = 100;

    glColor3f(1, 0, 0);
    for (float i = -10; i < 10; i += .0001) glVertex2i(radius * (i), radius * sin(i));
    glColor3f(0, 1, 0);
    for (float i = -10; i < 10; i += .0001) glVertex2i(radius * (i), radius * cos(i));
    glColor3f(0, 0, 1);
    for (float i = -10; i < 10; i += .0001) glVertex2i(radius * (i), radius * tan(i));

    glEnd();
    glFlush();
}

main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920/2, 1080/2);
    glutCreateWindow("circle");
    gluOrtho2D(-780, 780, -420, 420);
    glutDisplayFunc(display);
    glutMainLoop();
}
