import picodisplay as display


class Sprite:
    def __init__(self):
        self.x = 120 # out of 240 pixels
        self.y = 67 # out of 135 pixels
        self.pixels = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0]
        ]
        self.colour = {"r": 203, "g": 75, "b": 22}
        self.background = {"r": 7, "g": 54, "b": 66}

    def update(self):

        # clear screen
        display.set_pen(
            self.background["r"],
            self.background["g"],
            self.background["b"]
        )
        display.clear()

        # draw image in pixels
        display.set_pen(
            self.colour["r"],
            self.colour["g"],
            self.colour["b"]
        )
        x = self.x
        y = self.y
        for row in self.pixels:
            x = self.x
            for pixel in row:
                if pixel:
                    display.pixel(x, y)
                x += 1
            y += 1

        display.update()


def game_loop(sprite):
    while True:
        moved = True
        if display.is_pressed(display.BUTTON_A):
            sprite.x += 1
        elif display.is_pressed(display.BUTTON_B):
            sprite.x -= 1
        elif display.is_pressed(display.BUTTON_X):
            sprite.y += 1
        elif display.is_pressed(display.BUTTON_Y):
            sprite.y -= 1
        else:
            moved = False

        if moved:
            sprite.update()


if __name__ == "__main__":
    width = display.get_width()
    height = display.get_height()
    display_buffer = bytearray(width * height * 2)
    display.init(display_buffer)
    display.set_backlight(1.0)

    # initialise sprite
    sprite = Sprite()
    sprite.update()
    game_loop(sprite)
