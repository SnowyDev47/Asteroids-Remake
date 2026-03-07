## ASTEROIDS MAIN FILE
#
## IMPORTS

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #PLAYER
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #ASTEROID FIELD
    asteroid_field = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for it in drawable:
            it.draw(screen)
        for it in updatable:
            it.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player_instance) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
