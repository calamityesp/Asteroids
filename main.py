"""
Module Asteroids

Recreation of the asteroids game in Python

Classes:

Functions:

Usage example:
    Play Asteroids: This will use pygame to allow you to play asteroids
"""

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    """
    This is the main function for the asteroids game
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    while True:
        screen.fill("#000000")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (
            time_clock.tick(60) / 1000
        )  # keep game running at 60fps and store the time in second


if __name__ == "__main__":
    main()
