import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
SILVER = (192, 192, 192)
PURPLE = (128, 0, 128)
color_list = [BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, WHITE]

src_width = 600
src_height = 600

text = "red"

screen = pygame.display.set_mode((src_width, src_height))
pygame.display.set_caption('MS PAINT')


x = 0

color = color_list[x]
radius = 7
screen.fill(WHITE)


run = True
while run:

    for event in pygame.event.get():
        pygame.display.update(pygame.draw.rect(screen, SILVER, (0, src_height-150, src_width, 150)))
        pygame.draw.line(screen, BLACK, (0, src_height-150), (src_width, src_height-150), 1)
        pygame.display.update(pygame.draw.circle(screen, color_list[x], (src_width//2, src_height-75), radius, radius-1))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        color = color_list[x]
        if click[0] == 1:

            pygame.display.update(pygame.draw.circle(screen, color, mouse, radius, radius-1))

        if key[pygame.K_e]:
            screen.fill(color_list[x])

        if key[pygame.K_UP]:
            if radius < 75:
                radius += 1

            if radius == 75:
                radius = 7
        if key[pygame.K_DOWN]:
            if radius > 6:
                radius -= 1
            if radius == 6:
                radius = 75
            else:
                pass
        if key[pygame.K_r]:
            radius = 7

        if key[pygame.K_m]:
            radius = 75

        if key[pygame.K_RIGHT] and x < len(color_list) - 1:
            x += 1

        if key[pygame.K_LEFT] and x > 0:
            x -= 1
            
        else:
            pass

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
quit()
# E-key fills the screen with your current color
# The up and down arrow keys changes the brush size
# The left and right arrow keys changes the color
# R-key makes the brush size the smallest
# M-key makes the brush size the biggest
