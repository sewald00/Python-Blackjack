import pygame
from gamelogic import new_hand, playerturn

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Python Black Jack")
screen.fill((0, 51, 25))
pygame.mixer.init()
cardsound=pygame.mixer.Sound('cardPlace1.wav')


def main():
    new_hand()


if __name__ =='__main__':
    main()




