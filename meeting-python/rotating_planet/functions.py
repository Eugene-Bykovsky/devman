def set_green_color_black_back() -> None:
    """Устанавливает зеленый цвет текста на черном фоне"""
    print("\u001b[32m\u001b[40m", end="")


def set_white_color_black_back() -> None:
    """Устанавливает белый цвет текста на черном фоне"""
    print("\u001b[37m\u001b[40m", end="")


def clear_screen_and_move_cursor() -> None:
    """Очищает экран и двигает курсор в начало"""
    print("\033[2J\033[1;1H", end="")


def reset_color() -> None:
    """Сбрасывает цвет"""
    print("\u001b[0m", end="")


def render_planet(planet: str) -> None:
    """Рисует планету"""
    print(planet, end="")
