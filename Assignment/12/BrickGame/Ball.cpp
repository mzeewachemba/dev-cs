#include "Ball.h"
#include "MyGraphics.h"

// Implement ball
Ball::Ball(BrickArchitecture bgame) {
	this->brick_game = bgame;
	ball_start_pos_x = bgame.num_game_rectangles_width / 2 * 50;
	ball_start_pos_y = bgame.num_game_rectangles_height / 2 * 50;
	ball_end_pos_x = ball_start_pos_x + 25;
	ball_end_pos_y = ball_start_pos_y + 25;
	ball_y_direction = 1;
}

void Ball::respawnball() {
	ball_pos_y_increment = 10;
	ball_pos_x_increment = 25;
	MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
	ball_start_pos_x = brick_game.num_game_rectangles_width / 2 * 50;
	ball_start_pos_y = brick_game.num_game_rectangles_height / 2 * 50;
	ball_end_pos_x = ball_start_pos_x + 25;
	ball_end_pos_y = ball_start_pos_y + 25;
	MyGraphics::delay(25);
	MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_end_pos_x, ball_end_pos_y, 255, 255, 0, 255, 255, 0);
}

void Ball::display_lives(int lives) {
	MyGraphics::showConsoleCursor(0);
	for (int i = 1; i <= total_lives; i++) {
		MyGraphics::drawEllipse(i * 20 + 100, lives_displayer_y = (brick_game.num_game_rectangles_height * 50) + 450,
			i * 20 + 10 + 100, lives_displayer_y + 10, 0, 0, 0, 0, 0, 0);
	}
	for (int i = 1; i <= lives; i++) {
		MyGraphics::drawEllipse(i * 20 + 100, lives_displayer_y = (brick_game.num_game_rectangles_height * 50) + 450,
			i * 20 + 10 + 100, lives_displayer_y + 10, 255, 255, 0, 255, 255, 0);
	}
}

void Ball::ball() {
	bool angular_collision = false;
	bool boundary_collision = false;
	MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_end_pos_x, ball_end_pos_y, 255, 255, 0, 255, 255, 0);
	MyGraphics::delay(25);
	display_lives(total_lives);
	brick_game.display_boundary();
	brick_game.display_slate();
	int slate_mid;
	while (1) {
		MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_end_pos_x, ball_end_pos_y, 0, 0, 0, 0, 0, 0);
		ball_start_pos_y += ball_pos_y_increment;
		ball_end_pos_y = ball_start_pos_y + 25;
		if (angular_collision == true || boundary_collision == true) {
			ball_start_pos_x += ball_pos_x_increment;
			ball_end_pos_x = ball_start_pos_x + 25;
		}
		MyGraphics::delay(25);
		MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_end_pos_x, ball_end_pos_y, 255, 255, 0, 255, 255, 0);
		MyGraphics::delay(25);

		// ---detect if slate collided with the ball----
		if ((ball_end_pos_y >= brick_game.slate_start_y) && ((ball_start_pos_x >= brick_game.slate_start_x) && (ball_end_pos_x <= brick_game.slate_end_x))) {
			boundary_collision = false;
			angular_collision = false;
			ball_pos_y_increment = -1 * ball_pos_y_increment;
			ball_start_pos_y = ball_start_pos_y - 5;
			MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
			slate_mid = (brick_game.slate_end_x + brick_game.slate_start_x) / 2;
			if (ball_end_pos_x == slate_mid) { // will reflect straight upwards
				continue;
			}
			else {
				if (ball_end_pos_x > slate_mid) { // will reflect to the right side
					ball_pos_x_increment = 1 * ball_pos_x_increment;
					angular_collision = true;
					continue;
				}
				else {
					if (ball_end_pos_x < slate_mid) {
						ball_pos_x_increment = -1 * ball_pos_x_increment;
						angular_collision = true;
						continue;
					}
				}
			}
		}

		//--------check for collision with left, right boundary--------
// for right side boundary lets check end x coordinate
		if (ball_end_pos_x >= (brick_game.num_game_rectangles_width - 2) * 50 + 50) {
			boundary_collision = true; // ball collided with right boundary
			ball_pos_x_increment = -1 * ball_pos_x_increment;
			MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
			brick_game.display_boundary();
			ball_start_pos_x = ball_start_pos_x - 5;
		}

		// for left side boundary lets check start x coordinate
		if (ball_start_pos_x <= 50) {
			MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
			brick_game.display_boundary();
			ball_start_pos_x = ball_start_pos_x + 5;
			boundary_collision = true; // ball collided with left boundary
			ball_pos_x_increment = -1 * ball_pos_x_increment;
		}

		//----------end check for left right boundary---------------------------

		if (brick_game.brickcollision(ball_start_pos_x, ball_start_pos_y) == true) {
			// brickcollision(ball_end_pos_x, ball_start_pos_y);
			ball_pos_x_increment = 1 * ball_pos_x_increment;
			ball_pos_y_increment = -1 * ball_pos_y_increment;
			MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
			ball_start_pos_y = ball_start_pos_y + 60;
			brick_game.display_bricks();
			continue;
		}

		int slate_initial_y = ((brick_game.num_game_rectangles_height - 1) * 50) + 25;

		//if ((ball_start_pos_x >= 50 && ball_end_pos_x <= (num_game_rectangles_width - 2) * 50 + 50) && (ball_start_pos_y == 0))
		if ((ball_start_pos_x >= 50 && ball_end_pos_x <= (brick_game.num_game_rectangles_width - 2) * 50 + 50) && (ball_start_pos_y > slate_initial_y)) {
			// ball has moved beyond the slate at the bottom
			// increment miss slate count
			current_lives--;
			display_lives(current_lives);
			if (current_lives == 0) {
				MyGraphics::cls();
				break;
			}
			ball_pos_x_increment = 0 * ball_pos_x_increment;
			angular_collision = false;
			boundary_collision = false;
			respawnball(); // start ball in the middle
			brick_game.display_slate(); // start slate in the middle
		}

		if (ball_start_pos_y < 5) // ball has reached the top, reverse direction
		{
			MyGraphics::delay(1);
			MyGraphics::drawEllipse(ball_start_pos_x, ball_start_pos_y, ball_start_pos_x + 25, ball_start_pos_y + 25, 0, 0, 0, 0, 0, 0);
			MyGraphics::delay(1);
			ball_start_pos_y = ball_start_pos_y + 50;
			ball_pos_y_increment = -1 * ball_pos_y_increment;
		}

		char key = MyGraphics::getKey();
		brick_game.slate_movement(key);
		if (key == 'p') {
			do {
				MyGraphics::delay(1);
				key = MyGraphics::getKey();
			} while (key != 'r');
		}

		//compute_and_display_score(brick_game);
	}
}
