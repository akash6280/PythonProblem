import math
import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2
START_POSITION = 0
current_position = START_POSITION
no_of_plays =0
while current_position < 100:
    number_on_die = math.floor(random.random() * 10) % 6 + 1
    option = math.floor(random.random() * 10) % 3
    no_of_plays += 1
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
    print(current_position)

print("Player wins")
print(f"no of plays {no_of_plays}")
print(f"position at end {current_position}")
