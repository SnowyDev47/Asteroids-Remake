## ASTEROIDS MAIN FILE
#
## IMPORTS

import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Main Function

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #ScoreBoard
    player_score = 0
    score_font = pygame.font.SysFont("Arial", 36)



    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    #PLAYER
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #ASTEROID FIELD
    asteroid_field = AsteroidField()


    #Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("You quit!")
                print(f"Your score was: {player_score}")
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        scoreboard = score_font.render(f"Score: {player_score}", True, (255, 255, 255))
        screen.blit(scoreboard, (SCREEN_WIDTH / 2, 10))
        for it in drawable:
            it.draw(screen)
        for it in updatable:
            it.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player_instance) == True:
                log_event("player_hit")
                print("You died!")
                print(f"Your score was: {player_score}")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    player_score += 10
        pygame.display.update()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
