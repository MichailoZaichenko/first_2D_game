import pygame
import os

# Initialise
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game!")

# Some constants
FPS = 60
VELOSITY = 5
SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40 
BACKGROUND_COLLOR = (242, 243, 244)

# Images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'spaceship_red.png')), 270)
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT))

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# Controlling functions
def draw_window(red, yellow):
    WIN.fill(BACKGROUND_COLLOR)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()   


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)

    clock = pygame.time.Clock()
    # infinit window loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # left
            yellow.x -= VELOSITY
        if keys_pressed[pygame.K_d]: # right
            yellow.x += VELOSITY
        if keys_pressed[pygame.K_w]: # up
            yellow.y -= VELOSITY
        if keys_pressed[pygame.K_s]: # down
            yellow.y += VELOSITY
        draw_window(red, yellow)


    pygame.quit()

if __name__ == "__main__":
    main()