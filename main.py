import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        #Allow the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Fill the screen black
        screen.fill((0, 0, 0))

        #Draw player
        player.draw(screen)

        #Update screen
        pygame.display.flip()
        
        #Limit FPS to 60
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
