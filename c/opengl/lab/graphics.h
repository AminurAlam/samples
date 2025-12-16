#include <GL/freeglut.h>
#include <GL/glut.h>
#include <chrono>
#include <math.h>
#include <thread>

#define DETECT 0
#define WHITE 0
#define RED 1
#define BLUE 2
#define GREEN 3

// Drawing Functions
void arc(int x, int y, int stangle, int endangle, int radius);
void bar(int left, int top, int right, int bottom);
void bar3d(int left, int top, int right, int bottom, int depth, int topflag);
void circle(int x, int y, int radius);
void cleardevice();
void clearviewport();
void drawpoly(int n_points, int *points);
void ellipse(int x, int y, int stangle, int endangle, int xradius, int yradius);
void fillellipse(int x, int y, int xradius, int yradius);
void fillpoly(int n_points, int points[]);
void floodfill(int x, int y, int border);
void line(int x1, int y1, int x2, int y2);
void linerel(int dx, int dy);
void lineto(int x, int y);
void pieslice(int x, int y, int stangle, int endangle, int radius);
void putpixel(int x, int y, int color);
void rectangle(int left, int top, int right, int bottom);
void sector(int x, int y, int stangle, int endangle, int xradius, int yradius);

inline void cleardevice() { glClear(GL_COLOR_BUFFER_BIT); }
inline int getmaxx() { return 1920; }
inline int getmaxy() { return 1080; }
inline void delay(int msec) {
    std::this_thread::sleep_for(std::chrono::milliseconds(msec));
}
inline void initgraph(int *a, int *b) {
    glutInitWindowSize(1920, 1080);
    glutCreateWindow("graphics");
    gluOrtho2D(0, 1920, 1080, 0);
}
inline void putpixel(int x, int y, int color) {
    glBegin(GL_POINTS);

    switch (color) {
    case WHITE: glColor3f(1, 1, 1); break;
    case RED: glColor3f(1, 0, 0); break;
    case GREEN: glColor3f(0, 1, 0); break;
    case BLUE: glColor3f(0, 0, 1); break;
    }

    glVertex2i(x, y);
    glEnd();
    // glFlush();
}
inline void line(int x1, int y1, int x2, int y2) {
    glBegin(GL_LINES);
    glVertex2i(x1, y1);
    glVertex2i(x2, y2);
    glEnd();
    glFlush();
}
inline void rectangle(int left, int top, int right, int bottom) {
    int verts[] = {left, top, left, bottom, right, bottom, right, top};
    drawpoly(4, verts);
}
inline void circle(int x, int y, int radius) {
    glBegin(GL_POINTS);
    for (float i = 0; i < M_PI / 2; i += .01) {
        glVertex2i(radius * -sin(i) + x, radius * cos(i) + y);
        glVertex2i(radius * sin(i) + x, radius * -cos(i) + y);
        glVertex2i(radius * sin(i) + x, radius * cos(i) + y);
        glVertex2i(radius * -sin(i) + x, radius * -cos(i) + y);
    }
    glEnd();
    glFlush();
}
inline void
ellipse(int x, int y, int stangle, int endangle, int xradius, int yradius) {
    glBegin(GL_POINTS);
    for (float i = 0; i < M_PI / 2; i += .01) {
        // if (((float)stangle / 180 > i) || (i > (float)endangle / 180))
        // continue;
        glVertex2i(xradius * -sin(i) + x, yradius * cos(i) / 2 + y);
        glVertex2i(xradius * sin(i) + x, yradius * -cos(i) / 2 + y);
        glVertex2i(xradius * sin(i) + x, yradius * cos(i) / 2 + y);
        glVertex2i(xradius * -sin(i) + x, yradius * -cos(i) / 2 + y);
    }
    glEnd();
    glFlush();
};
inline void drawpoly(int n_points, int points[]) {
    glBegin(GL_LINES);
    for (int i = 0; i <= n_points; i = i + 2)
        line(points[i + 0], points[i + 1], points[i + 2], points[i + 3]);
    line(
        points[(n_points * 2) - 2], points[(n_points * 2) - 1], points[0],
        points[1]
    );
    glEnd();
    glFlush();
};

inline void
bar3d(int left, int top, int right, int bottom, int depth, int topflag) {
    rectangle(left, top, right, bottom);
    rectangle(left + depth, top + depth, right + depth, bottom + depth);
    line(left, top, left + depth, top + depth);
    line(right, top, right + depth, top + depth);
    line(left, bottom, left + depth, bottom + depth);
    line(right, bottom, right + depth, bottom + depth);
};

inline void drawgrid() {
    glBegin(GL_POINTS);
    for (int x = 0; x < 1920; x += 100) {
        for (int y = 0; y < 1080; y += 100) glVertex2i(x, y);
    }
    glEnd();

    int x = getmaxx(), y = getmaxy();

    glBegin(GL_LINES);
    {
        glVertex2i(x / 2, 0);
        glVertex2i(x / 2, y);
        glVertex2i(0, y / 2);
        glVertex2i(x, y / 2);
    }
    glEnd();

    glFlush();
}

// https://raw.githubusercontent.com/SagarGaniga/Graphics-Library/refs/heads/master/graphics.h

/*
// Miscellaneous Functions
// int getdisplaycolor(int color);
// int converttorgb(int color);
// void delay(int msec);
// void getarccoords(arccoordstype *arccoords);
// int getbkcolor();
// int getcolor();
// void getfillpattern(char *pattern);
// void getfillsettings(fillsettingstype *fillinfo);
// void getlinesettings(linesettingstype *lineinfo);
// int getmaxcolor();
// int getmaxheight();
// int getmaxwidth();
// int getmaxx();
// int getmaxy();
// bool getrefreshingbgi();
// int getwindowheight();
// int getwindowwidth();
// int getpixel(int x, int y);
// void getviewsettings(viewporttype *viewport);
// int getx();
// int gety();
// void moverel(int dx, int dy);
// void moveto(int x, int y);
// void refreshbgi(int left, int top, int right, int bottom);
// void refreshallbgi();
// void setbkcolor(int color);
// void setcolor(int color);
// void setfillpattern(char *upattern, int color);
// void setfillstyle(int pattern, int color);
// void setlinestyle(int linestyle, unsigned upattern, int thickness);
// void setrefreshingbgi(bool value);
// void setviewport(int left, int top, int right, int bottom, int clip);
// void setwritemode(int mode);

// Window Creation / Graphics Manipulation
// void closegraph(int wid = ALL_WINDOWS);
// void detectgraph(int *graphdriver, int *graphmode);
// void getaspectratio(int *xasp, int *yasp);
// char *getdrivername();
// int getgraphmode();
// int getmaxmode();
// char *getmodename(int mode_number);
// void getmoderange(int graphdriver, int *lomode, int *himode);
// void graphdefaults();
// char *grapherrormsg(int errorcode);
// int graphresult();
// void initgraph(int *graphdriver, int *graphmode, char *pathtodriver);
// int initwindow(
//     int width, int height, const char *title = "Windows BGI", int left = 0,
//     int top = 0, bool dbflag = false, bool closeflag = true
// );
// int installuserdriver(char *name, int *fp); // Not available in WinBGI
// int installuserfont(char *name);            // Not available in WinBGI
// int registerbgidriver(void *driver);        // Not available in WinBGI
// int registerbgifont(void *font);            // Not available in WinBGI
// void restorecrtmode();
// void setaspectratio(int xasp, int yasp);
// unsigned setgraphbufsize(unsigned bufsize); // Not available in WinBGI
// void setgraphmode(int mode);
// void showerrorbox(const char *msg = NULL);

// User Interaction
// int getch();
// int kbhit();

// User-Controlled Window Functions (winbgi.cpp)
// int getcurrentwindow();
// void setcurrentwindow(int window);

// Double buffering support (winbgi.cpp)
// int getactivepage();
// int getvisualpage();
// void setactivepage(int page);
// void setvisualpage(int page);
// void swapbuffers();

// Text Functions (text.cpp)
// void gettextsettings(struct textsettingstype *texttypeinfo);
// void outtext(char *textstring);
// void outtextxy(int x, int y, char *textstring);
// void settextjustify(int horiz, int vert);
// void settextstyle(int font, int direction, int charsize);
// void setusercharsize(int multx, int divx, int multy, int divy);
// int textheight(char *textstring);
// int textwidth(char *textstring);
// extern std::ostringstream bgiout;
// void outstream(std::ostringstream &out = bgiout);
// void outstreamxy(int x, int y, std::ostringstream &out = bgiout);

// Mouse Functions (mouse.cpp)
// void clearmouseclick(int kind);
// void clearresizeevent();
// void getmouseclick(int kind, int &x, int &y);
// bool ismouseclick(int kind);
// bool isresizeevent();
// int mousex();
// int mousey();
// void registermousehandler(int kind, void h(int, int));
// void setmousequeuestatus(int kind, bool status = true);

// Palette Functions
// palettetype *getdefaultpalette();
// void getpalette(palettetype *palette);
// int getpalettesize();
// void setallpalette(palettetype *palette);
// void setpalette(int colornum, int color);
// void setrgbpalette(int colornum, int red, int green, int blue);

// Color Macros
// #define IS_BGI_COLOR(v) (((v) >= 0) && ((v) < 16))
// #define IS_RGB_COLOR(v) ((v) & 0x03000000)
// #define RED_VALUE(v) int(GetRValue(converttorgb(v)))
// #define GREEN_VALUE(v) int(GetGValue(converttorgb(v)))
// #define BLUE_VALUE(v) int(GetBValue(converttorgb(v)))
// #undef COLOR
// int COLOR(int r, int g, int b); // No longer a macro
*/
