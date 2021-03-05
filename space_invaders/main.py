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


player_map = [
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
            for dx, pixel in enumerate(row):
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

    def remove_sprite(self):
        self.draw_sprite(colour=BACKGROUND_COLOUR)
        display.update()


class Row:
    def __init__(
        self,
        start_y,
        number,
        colour={"r": 255, "g": 255, "b": 255}
    ):
        self._x = WIDTH // number
        self._y = start_y
        self.dx = 0
        self.dy = 0
        self.colour = colour
        self.location = 0
        self.invaders = []
        for i in range(number):
            self.invaders.append(
                Sprite(start_x=self._x * (i + 1),
                       start_y=self._y))

    def update(self):
        # update row of invaders
        for invader in self.invaders:
            invader.dx = self.dx
            invader.dy = self.dy
            invader.update()

        # update position
        self._x += self.dx
        self._y += self.dy
        self.dx = self.dy = 0

    def move(self, step_size):
        if 0 <= self.location < 5:
            self.dx += step_size
            self.location += 1
            self.update()
        elif -5 <= self.location < 0:
            self.dx -= step_size
            self.location -= 1
            self.update()
        else:
            self.dy += step_size
            self.location = 0 if self.location < 0 else -1
            self.update()


def game_loop(step_time, step_size):
    # initialise objects
    enemy_row = Row(
        start_y=65,
        number=5,
        colour={"r": 0, "g": 0, "b": 255}
    )
    player = Sprite(
        start_x=120,
        start_y=100,
        pixel_map=player_map,
        colour={"r": 255, "g": 0, "b": 0}
    )
    enemy_row.update()
    player.update()

    # Loop
    while True:
        if display.is_pressed(display.BUTTON_Y):
            player.dx += step_size
        elif display.is_pressed(display.BUTTON_B):
            player.dx -= step_size
        elif display.is_pressed(display.BUTTON_X):
            # fire projectile
            pass
        elif display.is_pressed(display.BUTTON_A):
            # reset game state/return and display final score?
            return None

        player.update()
        enemy_row.move(step_size)
        sleep(step_time)


if __name__ == "__main__":
    global WIDTH, HEIGHT
    WIDTH = display.get_width()
    HEIGHT = display.get_height()
    display_buffer = bytearray(WIDTH * HEIGHT * 2)
    display.init(display_buffer)
    display.set_backlight(1.0)

    # Game_loop
    while True:
        game_loop(0.2, 5)
