import math
import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2
START_POSITION = 0
current_position_player1 = START_POSITION
current_position_player2 = START_POSITION
current_player = math.floor(random.random() * 10) % 2 + 1
while current_position_player1 < 100 and current_position_player2 < 100:
    number_on_die = math.floor(random.random() * 10) % 6 + 1
    option = math.floor(random.random() * 10) % 3
    if option == NO_PLAY:
        pass
    elif option == LADDER:
        if current_player == 1:
            if current_position_player1 + number_on_die > 100:
                pass
            else:
                current_position_player1 += number_on_die
            current_player = 1
        if current_player == 2:
            if current_position_player2 + number_on_die > 100:
                pass
            else:
                current_position_player2 += number_on_die
            current_player = 2

    else:
        if current_player == 1:
            current_position_player1 -= number_on_die
            if current_position_player1 < 0:
                current_position_player1 = 0
            current_player = 2

        else :
            current_position_player2 -= number_on_die
            if current_position_player2 < 0:
                current_position_player2 = 0
            current_player = 1

    if current_position_player1 == 100 or current_position_player2 == 100:
        break

if current_position_player1 == 100:
    print("Player 1 wins")
else:
    print("Player 2 wins")
