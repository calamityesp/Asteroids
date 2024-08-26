import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from util import Util


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0
    util = Util()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    util.display_start_msg()
    pygame.init()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("#000000")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (
            time_clock.tick(60) / 1000
        )  # keep game running at 60fps and store the time in second


if __name__ == "__main__":
    main()
