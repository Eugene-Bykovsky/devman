import time

from frames import PLANETS
from functions import (
    clear_screen_and_move_cursor,
    render_planet,
    reset_color,
    set_green_color_black_back,
    set_white_color_black_back,
)

set_green_color_black_back()
clear_screen_and_move_cursor()

for planet in PLANETS:
    render_planet(planet)
    time.sleep(0.7)
    clear_screen_and_move_cursor()

set_white_color_black_back()
print("THE END")
reset_color()
