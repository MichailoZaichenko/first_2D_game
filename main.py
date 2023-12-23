import pygame
import os

# Initialise
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game!")

# Colors
BACKGROUND_COLLOR = (242, 243, 244)
BLACK = (0,0,0)
# Some constants
FPS = 60
VELOSITY = 5
BULLET_VELOSITY = 8
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40 
BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)

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
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()   

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOSITY > 0: # left
        yellow.x -= VELOSITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOSITY + yellow.width < BORDER.x: # right
        yellow.x += VELOSITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOSITY > 0: # up
        yellow.y -= VELOSITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOSITY + yellow.height < HEIGHT - 20: # down
        yellow.y += VELOSITY

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOSITY > BORDER.x + BORDER.width: # left
        red.x -= VELOSITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOSITY + red.width < WIDTH: # right
        red.x += VELOSITY
    if keys_pressed[pygame.K_UP] and red.y - VELOSITY > 0: # up
        red.y -= VELOSITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOSITY + red.height < HEIGHT - 10: # down
        red.y += VELOSITY

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)

    red_bullets = []
    yellow_bullets =[]

    clock = pygame.time.Clock()
    # infinit window loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)


    pygame.quit()

if __name__ == "__main__":
    main()