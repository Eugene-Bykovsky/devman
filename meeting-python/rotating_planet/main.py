import time

from frames import PLANETS
from functions import (
    clear_screen_and_move_cursor,
    render_planet,
    reset_color,
    set_green_color_black_back,
    set_white_color_black_back,
)

for planet in PLANETS:
    set_green_color_black_back()
    render_planet(planet)
    time.sleep(1)
    clear_screen_and_move_cursor()

set_white_color_black_back()
print("THE END")
reset_color()
