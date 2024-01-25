#pragma once

#ifndef MYGRAPHICS_H_
#define MYGRAPHICS_H_

#include <windows.h>

class MyGraphics {
public:
    static void drawLine(int x1, int x2, int y1, int y2, int colour); // draws a line between two points given their x-y coordinates in gray-scale
    static void drawLine(int x1, int x2, int y1, int y2, int r, int g, int b); // draws a line between two points given their x-y coordinates using RGB colouring

    //static void drawRectangle(int x1, int y1, int x2, int y2, int R, int G, int B, int FR, int FG, int FB); // draws a rectangle using top-left and bottom-right x-y coordinates with a border using RGB colouring
    static void drawRectangle(int x1, int y1, int x2, int y2, int R, int G, int B, int FR, int FG, int FB); // draws a rectangle using top-left and bottom-right x-y coordinates with separate border and fill colours

    static void drawEllipse(int x1, int y1, int x2, int y2, int R, int G, int B); // draws a rectangle-bounded ellipse using top-left and bottom-right x-y coordinates with a border using RGB colouring
    static void drawEllipse(int x1, int y1, int x2, int y2, int R, int G, int B, int FR, int FG, int FB); // draw a rectangle-bounded ellipse using top-left and bottom-right x-y coordinates with separate border and fill colours

    static void cls(); // clears the screen
    static void delay(int ms); // waits for some time (in milli-seconds)
    static char getKey(); // gets key typed into the console without waiting for the input
    static void getWindowDimensions(int& width, int& height); // gets width and height of the window
    static void getConsoleWindowDimensions(int& width, int& height); // gets width and height of console window (in character mode)
    static void gotoxy(int x, int y); // sets console cursor on given x-y coordinates
    static void showConsoleCursor(bool showFlag); // shows or hides the cursor
};

#endif /* MYGRAPHICS_H_ */
