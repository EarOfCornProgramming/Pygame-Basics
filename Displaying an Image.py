import pygame

pygame.init()

display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
FPS = 50

def game():
    image = pygame.image.load("Ear Of Corn.png").convert_alpha()
    image = pygame.transform.scale(image, (1000, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 0, 0))
        display.blit(image, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()






















