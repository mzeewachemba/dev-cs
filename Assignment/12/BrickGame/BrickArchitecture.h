#pragma once
class BrickArchitecture
{
	int num_brick_rows = 3;
	int num_brick_coloumns = 12;
	//int num_game_rectangles_height = 12;
	//int num_game_rectangles_width = num_brick_coloumns + 2;
	//int brick_visible[3][12];
	int brick_coordinate_x_start[3][12];
	int brick_coordinate_y_start[3][12];
	int brick_coordinate_x_end[3][12];
	int brick_coordinate_y_end[3][12];
	/*int slate_start_x = 0;
	int slate_end_x;
	int slate_end_y;
	int slate_start_y = 0;*/
public:
	int slate_start_x = 0;
	int slate_end_x;
	int slate_end_y;
	int slate_start_y = 0;
	int num_game_rectangles_height = 12;
	int num_game_rectangles_width = num_brick_coloumns + 2;
	int brick_visible[3][12];
	BrickArchitecture(); // constructor
	//storing brick coordnates, side,slate
	//create brick,boundary and ctrl slate movcement
	//detects collision
	void display_boundary();
	void display_bricks();
	void display_slate();
	void slate_movement(char input);
	bool brickcollision(int x, int y);
};