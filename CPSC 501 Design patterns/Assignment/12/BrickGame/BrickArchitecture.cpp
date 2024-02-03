#include "BrickArchitecture.h"
#include "MyGraphics.h"

//implements brickarchitecture
BrickArchitecture::BrickArchitecture()
{
    for (int i = 0; i < num_brick_rows; i++)
    {
        for (int j = 0; j < num_brick_coloumns; j++)
        {
            brick_coordinate_x_start[i][j] = j * 50 + 50;
            brick_coordinate_y_start[i][j] = i * 50;
            brick_coordinate_x_end[i][j] = brick_coordinate_x_start[i][j] + 50;
            brick_coordinate_y_end[i][j] = brick_coordinate_y_start[i][j] + 50;
            brick_visible[i][j] = 1; // all bricks are visible at the start
        }
    }
    // display_slate();
}

void BrickArchitecture::display_boundary()
{
    for (int i = 0; i < num_game_rectangles_height; i++)
        MyGraphics::drawRectangle(0, i * 50, 50, i * 50 + 50, 255, 0, 0, 255, 0, 0);

    for (int j = 0; j < num_game_rectangles_height; j++)
        MyGraphics::drawRectangle((num_game_rectangles_width - 1) * 50, j * 50, num_game_rectangles_width * 50, j * 50 + 50, 255, 0, 0, 255, 0, 0);
}

void BrickArchitecture::display_bricks()
{
    for (int i = 0; i < num_brick_rows; i++)
    {
        for (int j = 0; j < num_brick_coloumns; j++)
        {
            if (brick_visible[i][j] == 1)
            {
                MyGraphics::drawRectangle(brick_coordinate_x_start[i][j],
                    brick_coordinate_y_start[i][j],
                    brick_coordinate_x_end[i][j],
                    brick_coordinate_y_end[i][j], 0, 0, 0, 0, 150, 255);
                MyGraphics::delay(1);
            }
            else
            {
                MyGraphics::drawRectangle(brick_coordinate_x_start[i][j],
                    brick_coordinate_y_start[i][j],
                    brick_coordinate_x_end[i][j],
                    brick_coordinate_y_end[i][j], 0, 0, 0, 0, 0, 0);
                MyGraphics::delay(1);
            }
        }
    }
}

void BrickArchitecture::display_slate()
{
    MyGraphics::drawRectangle(slate_start_x, slate_start_y, slate_end_x, slate_end_y, 0, 0, 0, 0, 0, 0);

    MyGraphics::drawRectangle(((num_game_rectangles_width / 2) - 1) * 50,
        ((num_game_rectangles_height - 1) * 50) + 25,
        (((num_game_rectangles_width / 2) - 1) * 50) + 100,
        (((num_game_rectangles_height - 1) * 50)) + 25 + 25, 255, 255, 255, 255, 255, 255);

    slate_start_x = ((num_game_rectangles_width / 2) - 1) * 50;
    slate_start_y = ((num_game_rectangles_height - 1) * 50) + 25;
    slate_end_y = slate_start_y + 25;
    slate_end_x = slate_start_x + 100;
}

void BrickArchitecture::slate_movement(char input)
{
    slate_end_y = slate_start_y + 25;

    if (input == 'd') // move slate right
    {
        if (slate_start_x < (num_game_rectangles_width - 3) * 50)
        {
            slate_end_x = slate_start_x + 100;
            MyGraphics::drawRectangle(slate_start_x, slate_start_y, slate_end_x, slate_end_y, 0, 0, 0, 0, 0, 0);
            slate_start_x = slate_start_x + 50;
            MyGraphics::drawRectangle(slate_start_x, slate_start_y, slate_end_x += 50, slate_end_y, 255, 255, 255, 255, 255, 255);
        }
    }

    if (input == 'a') // move slate left
    {
        if (slate_start_x > 50)
        {
            MyGraphics::drawRectangle(slate_start_x, slate_start_y, slate_end_x, slate_end_y, 0, 0, 0, 0, 0, 0);
            slate_start_x = slate_start_x - 50;
            MyGraphics::drawRectangle(slate_start_x, slate_start_y, slate_end_x -= 50, slate_end_y, 255, 255, 255, 255, 255, 255);
        }
    }
}

bool BrickArchitecture::brickcollision(int x, int y)
{
    bool brickcollision = false;
    for (int i = 0; i < num_brick_rows; i++)
    {
        for (int j = 0; j < num_brick_coloumns; j++)
        {
            if ((x >= brick_coordinate_x_start[i][j] && x <= brick_coordinate_x_end[i][j]) &&
                (y <= brick_coordinate_y_end[i][j]))
            {
                if (brick_visible[i][j] == 1)
                {
                    MyGraphics::drawRectangle(brick_coordinate_x_start[i][j],
                        brick_coordinate_y_start[i][j],
                        brick_coordinate_x_end[i][j],
                        brick_coordinate_y_end[i][j], 0, 0, 0, 0, 0, 0);
                    brick_visible[i][j] = 0;
                    brickcollision = true;
                    return brickcollision;
                }
            }
            else
                continue;
        }
    }
    return brickcollision;
}
