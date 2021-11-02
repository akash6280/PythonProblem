import math
import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2
START_POSITION = 0
current_position = START_POSITION
while current_position < 100:
    number_on_die = math.floor(random.random() * 10) % 6 + 1
    option = math.floor(random.random() * 10) % 3

    if option == NO_PLAY:
        pass
    elif option == LADDER:
        if current_position + number_on_die > 100:
            pass
        else:
            current_position += number_on_die
    else:
        current_position -= number_on_die
        if current_position < 0:
            current_position = 0
    if current_position == 100:
        break

print("Player wins")
print(f"position at end {current_position}")
