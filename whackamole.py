import pygame
import math
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("whackamole-template/mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #if it doesnt like it, remove this
        rColor = random.randint(50, 255)
        gColor = random.randint(50, 255)
        bColor = random.randint(50, 255)

        moleX = 0
        moleY = 0

        x, y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
            
            color = "black"
            defaultColor = "light green"

            #screen.fill([rColor, gColor, bColor])
            screen.fill(defaultColor)

            for x1 in range(32, 640, 32):
                pygame.draw.line(screen, color, (x1,0), (x1,512))
            for y1 in range(32, 512, 32):
                pygame.draw.line(screen, color, (0,y1), (640,y1))
            

            if x > moleX and x < moleX + 32 and y > moleY and y < moleY + 32:
                moleX = random.randint(1,19)*32
                moleY = random.randint(1,15)*32
                rColor = random.randint(50, 255)
                gColor = random.randint(50, 255)
                bColor = random.randint(50, 255)

            screen.blit(mole_image, mole_image.get_rect(topleft=(3+moleX,2+moleY)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
