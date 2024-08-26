import pygame

from asteroidField import AsteroidField
from asteroids import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shots import Shot
from util import Util


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    util = Util()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    util.display_start_msg()
    pygame.init()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if player.check_collision(ast):
                print("Game Over")
                return
            for bullet in shots:
                if ast.check_collision(bullet):
                    ast.split()
                    bullet.kill()

        screen.fill("#000000")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (
            time_clock.tick(60) / 1000
        )  # keep game running at 60fps and store the time in second


if __name__ == "__main__":
    main()
