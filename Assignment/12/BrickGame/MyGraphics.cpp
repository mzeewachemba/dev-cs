#include "MyGraphics.h"

void MyGraphics::drawLine(int x1, int y1, int x2, int y2, int colour) {
    drawLine(x1, y1, x2, y2, colour, colour, colour);
}

void MyGraphics::drawLine(int x1, int y1, int x2, int y2, int R, int G, int B) {
    HWND consoleHandle = GetConsoleWindow();
    HDC deviceContext = GetDC(consoleHandle);
    HPEN pen = CreatePen(PS_SOLID, 2, RGB(R, G, B));
    SelectObject(deviceContext, pen);
    MoveToEx(deviceContext, x1, y1, NULL);
    LineTo(deviceContext, x2, y2);
    ReleaseDC(consoleHandle, deviceContext);
    DeleteObject(pen);
}

void MyGraphics::drawRectangle(int x1, int y1, int x2, int y2, int R, int G, int B, int FR, int FG, int FB) {
    HWND consoleHandle = GetConsoleWindow();
    HDC deviceContext = GetDC(consoleHandle);
    HPEN pen = CreatePen(PS_SOLID, 2, RGB(R, G, B));
    SelectObject(deviceContext, pen);
    HBRUSH brush = CreateSolidBrush(RGB(FR, FG, FB));
    SelectObject(deviceContext, brush);
    Rectangle(deviceContext, x1, y1, x2, y2);
    ReleaseDC(consoleHandle, deviceContext);
    DeleteObject(pen);
    DeleteObject(brush);
}

void MyGraphics::drawEllipse(int x1, int y1, int x2, int y2, int R, int G, int B) {
    drawEllipse(x1, y1, x2, y2, R, G, B, 0, 0, 0);
}

void MyGraphics::drawEllipse(int x1, int y1, int x2, int y2, int R, int G, int B, int FR, int FG, int FB) {
    HWND consoleHandle = GetConsoleWindow();
    HDC deviceContext = GetDC(consoleHandle);
    HPEN pen = CreatePen(PS_SOLID, 2, RGB(R, G, B));
    SelectObject(deviceContext, pen);
    HBRUSH brush = CreateSolidBrush(RGB(FR, FG, FB));
    SelectObject(deviceContext, brush);
    Ellipse(deviceContext, x1, y1, x2, y2);
    ReleaseDC(consoleHandle, deviceContext);
    DeleteObject(pen);
    DeleteObject(brush);
}

void MyGraphics::cls() {
    COORD coordScreen = { 0, 0 };
    DWORD cCharsWritten;
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    DWORD dwConSize;
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    if (!GetConsoleScreenBufferInfo(consoleHandle, &csbi)) {
        return;
    }
    dwConSize = csbi.dwSize.X * csbi.dwSize.Y;
    FillConsoleOutputCharacter(consoleHandle, (TCHAR)' ', dwConSize, coordScreen, &cCharsWritten);
}

void MyGraphics::delay(int ms) {
    Sleep(ms);
}

char MyGraphics::getKey() {
    HANDLE consoleHandle = GetStdHandle(STD_INPUT_HANDLE);
    DWORD size = 1;
    INPUT_RECORD input[1];
    DWORD events = 0;
    char key = '\0';
    if (PeekConsoleInput(consoleHandle, input, size, &events)) {
        if (input[0].EventType == KEY_EVENT) {
            key = input[0].Event.KeyEvent.uChar.AsciiChar;
            FlushConsoleInputBuffer(consoleHandle);
            return key;
        }
    }
    return key;
}

void MyGraphics::getWindowDimensions(int& width, int& height) {
    HWND consoleHandle = GetConsoleWindow();
    RECT rc;
    GetClientRect(consoleHandle, &rc);
    width = rc.right;
    height = rc.bottom;
}

void MyGraphics::getConsoleWindowDimensions(int& width, int& height) {
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    if (!GetConsoleScreenBufferInfo(consoleHandle, &csbi)) {
        return;
    }
    width = csbi.srWindow.Right;
    height = csbi.srWindow.Bottom;
}

void MyGraphics::gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void MyGraphics::showConsoleCursor(bool flag) {
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO cursorInfo;
    GetConsoleCursorInfo(consoleHandle, &cursorInfo);
    cursorInfo.bVisible = flag;
    SetConsoleCursorInfo(consoleHandle, &cursorInfo);
}
