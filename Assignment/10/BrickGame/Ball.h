#pragma once
#include "BrickArchitecture.h"
class Ball
{
	int ball_start_pos_x;
	int ball_start_pos_y;
	int ball_end_pos_y;
	int ball_end_pos_x;
	int ball_pos_y_increment = 10;
	int ball_pos_x_increment = 25;
	int ball_y_direction = 0; // 0 is down, 1 is up
	int total_lives = 3;
	int total_score = 0;
	int current_lives = 3;
	int lives_displayer_x = 1, lives_displayer_y = 1;
	BrickArchitecture brick_game;
public:
	Ball(BrickArchitecture bgame);
	//for monitoring the status of the game
	void respawnball();
	void ball();
	void display_lives(int lives);
};
