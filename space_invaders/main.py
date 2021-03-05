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


projectile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
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

        # display.update()

    def remove_sprite(self):
        self.draw_sprite(colour=BACKGROUND_COLOUR)
        # display.update()


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
                Sprite(start_x=self._x * i,
                       start_y=self._y,
                       colour=colour))

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


class Projectile(Sprite):
    def __init__(
        self,
        start_x,
        start_y,
        pixel_map=projectile_map,
        colour={"r": 255, "g": 0, "b": 0}
    ):
        super().__init__(
            start_x=start_x,
            start_y=start_y,
            pixel_map=pixel_map,
            colour=colour
        )

    def move(self, step_size):
        self.dy -= step_size
        self.update()


class Player(Sprite):
    def __init__(
        self,
        start_x=120,
        start_y=67,
        pixel_map=space_invader_map,
        colour={"r": 255, "g": 255, "b": 255}
    ):
        super().__init__(
            start_x=start_x,
            start_y=start_y,
            pixel_map=pixel_map,
            colour=colour
        )

    def fire_projectile(self, colour={"r": 0, "g": 255, "b": 0}):
        projectile = Projectile(
            start_x=self._x,
            start_y=self._y,
            pixel_map=projectile_map,
            colour=colour
        )
        return projectile

def clear_display():
    display.set_pen(
        BACKGROUND_COLOUR["r"],
        BACKGROUND_COLOUR["g"],
        BACKGROUND_COLOUR["b"]
    )
    display.clear()
    display.update()


def game_loop(step_time, step_size):
    # initialise objects
    enemy_row = Row(
        start_y=0,
        number=5,
        colour={"r": 0, "g": 0, "b": 255}
    )
    player = Player(
        start_x=120,
        start_y=110,
        pixel_map=player_map,
        colour={"r": 255, "g": 0, "b": 0}
    )
    enemy_row.update()
    player.update()

    # Loop
    count = 0
    projectiles = []
    while True:
        if display.is_pressed(display.BUTTON_Y):
            player.dx += step_size
        elif display.is_pressed(display.BUTTON_B):
            player.dx -= step_size
        elif display.is_pressed(display.BUTTON_X):
            # fire projectile
            projectiles.append(player.fire_projectile())
            pass
        elif display.is_pressed(display.BUTTON_A):
            # reset game state/return and display final score?
            clear_display()
            return None

        player.update()
        
        # move enemy every 5 steps
        if count % 5 == 0:
            enemy_row.move(step_size)

        if projectiles:
            for projectile in projectiles:
                projectile.move(step_size)

        count = count + 1 if count < 256 else 0

        display.update()
        sleep(step_time)


if __name__ == "__main__":
    global WIDTH, HEIGHT
    WIDTH = display.get_width()
    HEIGHT = display.get_height()
    display_buffer = bytearray(WIDTH * HEIGHT * 2)
    display.init(display_buffer)
    display.set_backlight(1.0)
    clear_display()

    # Game_loop
    while True:
        game_loop(0.2, 5)
