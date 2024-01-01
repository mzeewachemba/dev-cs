// BrickGame.cpp: This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include "MyGraphics.h"
#include "BrickArchitecture.h"
#include "Ball.h"
using namespace std;

char key;
int slate_mid;
int num_brick_coloumns = 12;
int num_brick_rows = 3;
int num_game_rectangles_height = 12;
int num_game_rectangles_width = num_brick_coloumns + 2;
int total_lives = 3;
int total_score = 0;
int current_lives = 3;

void compute_and_display_score(BrickArchitecture brick_game);

void compute_and_display_score(BrickArchitecture brick_game)
{
    int count = 0;
    int updated_score;
    for (int i = 0; i < num_brick_rows; i++)
    {
        for (int j = 0; j < num_brick_coloumns; j++)
        {
            if (brick_game.brick_visible[i][j] == 0)
            {
                count++;
            }
        }
    }
    updated_score = count * 10;
    total_score = updated_score;
    cout << "\r" << "TOTAL SCORE: " << total_score << std::flush;
}

int main()
{
    cout << "WELCOME TO BRICK BREAKER" << endl << "INSTRUCTIONS: PRESS A TO MOVE LEFT AND PRESS D TO MOVE RIGHT" << endl;
    cout << "PRESS X TO START PLAYING: ";
    char start;
    do
    {
        cin >> start;
        if (start == 'x')
        {
            MyGraphics::cls();
            MyGraphics::gotoxy(0, (num_game_rectangles_height) * 2 + 2);
        }
    } while (start != 'x');

    MyGraphics::showConsoleCursor(0);
    current_lives = total_lives;
    BrickArchitecture brick_game;
    Ball ballc(brick_game);
    brick_game.display_boundary();
    brick_game.display_bricks();
    brick_game.display_slate();
    cout << "LIVES : \n" << endl;
    ballc.ball();

    int w, h;
    MyGraphics::getWindowDimensions(w, h);
    MyGraphics::gotoxy(w / 2, h / 2);
    cout << "GAME OVER, BETTER LUCK NEXT TIME :)";

    return 0;
}