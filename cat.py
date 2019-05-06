import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect, KEYUP


pygame.init()
SURFACE = pygame.display.set_mode((1080, 720))
pygame.key.set_repeat(5, 5)
FPSCLOCK = pygame.time.Clock()

blocks = []

def move():
    for block in blocks:
        block[0] -= 6


def main():
    """ main routine """
    cats_sequence = pygame.image.load("cats.png")
    images = []
    for index in range(12):
        image = pygame.Surface([400, 200], pygame.SRCALPHA, 32)
        image.blit(cats_sequence, (0, 0), Rect(0, index * 200, 400, 200))
        images.append(image)

    for xpos in range(10, 20):
        random_num = randint(5, 9)
        blocks.append(Rect(xpos*30*random_num, 440, 30, 40))

    jump = False
    myfont = pygame.font.SysFont(None, 80)
    pos_y = 297
    game_over = False
    counter = 0
    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    jump = True
            elif event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    jump = False
                        

        if not game_over:
            move()
            if jump:
                pos_y -= 20
            elif not jump and pos_y <= 297:
                pos_y += 20

                

            if pos_y < 130 or blocks[0].left <= pos_y  :
                game_over = True

        SURFACE.fill((255, 255, 255))
        pygame.draw.rect(SURFACE, (255, 0, 0), (0, 480, 1080, 200))
        pygame.draw.rect(SURFACE, (255, 0, 0), (0, 0, 1080, 130))
        if game_over:
            message = myfont.render("Game Over!!", True, (0, 255, 255))
            SURFACE.blit(message, (600, 360))
        

        """まず一個のブロックから作る"""
        for block in blocks:
            pygame.draw.rect(SURFACE, (75, 75, 75), block)

        SURFACE.blit(images[counter % 12], (100, pos_y))
        counter += 1

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
