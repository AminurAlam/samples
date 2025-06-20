#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_LINES);
    float r,g,b, x, X;

    for (float rgb = 0; rgb < 1; rgb += (float)1/19200) {
        x = rgb*2 - 1;
        X = (rgb+(float)1/19200)*2 - 1;

        glColor3f(
            (0.00f <= rgb && rgb < 0.50f) ? 1-rgb*2 : 0,
            (0.25f <= rgb && rgb < 0.75f) ? (rgb < 0.50f)?(rgb-.25)*4:1-(rgb-.50)*4: 0,
            (0.50f <= rgb && rgb < 1.00f) ? (rgb-.5)*2 : 0
        );
        glVertex2f(x, 1); glVertex2f(X, (float)4/3 - 1);
        glColor3f(
            (0.25f <= rgb && rgb < 0.75f) ? (rgb < 0.50f)?(rgb-.25)*4:1-(rgb-.50)*4: 0,
            (0.50f <= rgb && rgb < 1.00f) ? (rgb-.5)*2 : 0,
            (0.00f <= rgb && rgb < 0.50f) ? 1-rgb*2 : 0
        );
        glVertex2f(x, (float)4/3 - 1); glVertex2f(X, (float)2/3 - 1);
        glColor3f(
            (0.50f <= rgb && rgb < 1.00f) ? (rgb-.5)*2 : 0,
            (0.00f <= rgb && rgb < 0.50f) ? 1-rgb*2 : 0,
            (0.25f <= rgb && rgb < 0.75f) ? (rgb < 0.50f)?(rgb-.25)*4:1-(rgb-.50)*4: 0
        );
        glVertex2f(x, (float)2/3 - 1); glVertex2f(X, -1);

    }
    glEnd();
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(1920/2, 1080/3);
    glutCreateWindow("rgb3x3");
    glutDisplayFunc(display);
    glutMainLoop();
}
