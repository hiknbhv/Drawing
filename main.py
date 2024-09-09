import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (200, 10, 200)
PURPLE = (128, 0, 225)
ORANGE = (255, 128, 0)

display_surface.fill(WHITE)

CENTER = (200, 225)
RADIUS = 100

pygame.draw.circle(display_surface, BLACK, CENTER, RADIUS)

CENTER2 = (400,225)
pygame.draw.circle(display_surface, BLACK, CENTER2, RADIUS)

CENTER3 = (300,350)
RADIUS2 = 150
pygame.draw.circle(display_surface, BLACK, CENTER3, RADIUS2)

CENTER4 = (275,200)
RADIUS3 = 40
pygame.draw.circle(display_surface, MAGENTA, CENTER4, RADIUS3)

CENTER5 = (325,200)
pygame.draw.circle(display_surface, MAGENTA, CENTER5, RADIUS3)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()