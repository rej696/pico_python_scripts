from time import sleep
import picodisplay as display


BACKGROUND_COLOUR = {"r": 0, "g": 0, "b": 0}


space_invader_map = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
]


class Sprite:
    def __init__(
            self,
            start_x=120,
            start_y=67,
            pixel_map=space_invader_map,
            colour={"r": 255, "g": 255, "b": 255}
    ):
        self._x = start_x  # out of 240 pixel_map
        self._y = start_y  # out of 135 pixel_map
        self.dx = 0
        self.dy = 0
        self.pixel_map = pixel_map
        self.colour = colour

    def draw_sprite(self, colour):
        display.set_pen(
            colour["r"],
            colour["g"],
            colour["b"]
        )

        for dy, row in enumerate(self.pixel_map):
            for dx, pixel in enumerate(self.pixel_map):
                if pixel:
                    display.pixel(self._x + dx, self._y + dy)

    def update(self):
        # clear old sprite
        self.draw_sprite(colour=BACKGROUND_COLOUR)

        # update new x and y coords
        self._x += self.dx
        self._y += self.dy

        # reset dy and dx values
        self.dx = self.dy = 0

        # draw sprite at new location
        self.draw_sprite(colour=self.colour)

        display.update()


def game_loop(sprite, step_time, step_size):
    while True:
        moved = True
        if display.is_pressed(display.BUTTON_A):
            sprite.x += step_size
        elif display.is_pressed(display.BUTTON_B):
            sprite.x -= step_size
        elif display.is_pressed(display.BUTTON_X):
            sprite.y += step_size
        elif display.is_pressed(display.BUTTON_Y):
            sprite.y -= step_size
        else:
            moved = False

        if moved:
            sprite.update()
            sleep(step_time)


if __name__ == "__main__":
    width = display.get_width()
    height = display.get_height()
    display_buffer = bytearray(width * height * 2)
    display.init(display_buffer)
    display.set_backlight(1.0)

    # initialise sprite
    sprite = Sprite()
    sprite.update()
    game_loop(sprite, 0.2, 5)
