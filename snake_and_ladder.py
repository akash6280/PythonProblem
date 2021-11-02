import math
import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2
START_POSITION = 0
current_position = START_POSITION
number_on_die = math.floor(random.random() * 10) % 6 + 1
print(f"Number on die {number_on_die}")

option = math.floor(random.random() * 10) % 3

if option == NO_PLAY:
    pass
elif option == LADDER:
    current_position += number_on_die
else:
    current_position -= number_on_die
print(f"current position {current_position}")
