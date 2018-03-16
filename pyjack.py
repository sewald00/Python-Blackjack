import pygame
from pygame.locals import *
import spritesheet
from random import shuffle
from cards import *

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Python Black Jack")
screen.fill((0, 51, 25))




shuffle(deck)
cardCount=0
playerHand=[]
playerHand.append(deck[0])
playerHand.append(deck[1])
handValue=str(playerHand[0].Number+playerHand[1].Number)

computerHand=(deck[cardCount+2],deck[cardCount+3])






ss = spritesheet.spritesheet('cards.jpg')
# Sprite is 16x16 pixels at location 0,0 in the file...
image = ss.image_at((playerHand[0].X,playerHand[0].Y, 50, 75))
image2= ss.image_at((playerHand[1].X,playerHand[1].Y, 50, 75))
cardD1= ss.image_at((20,384, 50, 75))
cardD2= ss.image_at((computerHand[1].X,computerHand[1].Y, 50, 75))

screen.blit(image,(350,250))
screen.blit(image2,(290,250))
screen.blit(cardD1,(290,50))
screen.blit(cardD2,(350,50))
pygame.display.flip()

myfont = pygame.font.SysFont("monospace", 20)

# render text
label = myfont.render(handValue, 1, (255,255,0))
screen.blit(label, (333, 350))
pygame.display.flip()
done=False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop




