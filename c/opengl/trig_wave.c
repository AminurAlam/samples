#include <GL/glut.h>
#include <math.h>

void display() {
    int radius = 200;

    for (int phase = 0; phase < 6*radius; phase++) {
        glClear(GL_COLOR_BUFFER_BIT);
        glBegin(GL_LINES);
        glColor3f(0.2, 0.2, 0.2);
        glVertex2i(-780,0); glVertex2i(780,0);
        glVertex2i(0,-420); glVertex2i(0,420);
        glEnd();
        glBegin(GL_POINTS);
        glColor3f(0, 1, 0);
        for (float i = -10; i < 4; i += .0001)
            glVertex2i(((phase%radius*2)*M_PI)+radius*(i), radius*sin(i));
        glEnd();
        glFlush();
    }
}

main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920/2, 1080/2);
    glutCreateWindow("wave");
    gluOrtho2D(-780, 780, -420, 420);
    glutDisplayFunc(display);
    glutMainLoop();
}
