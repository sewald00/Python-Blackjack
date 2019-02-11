from random import shuffle
import spritesheet
import pygame
import time
from cards import deck

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Python Black Jack")
screen.fill((0, 51, 25))
pygame.mixer.init()
cardsound=pygame.mixer.Sound('cardPlace1.wav')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

def new_hand():
    screen.fill((0, 51, 25))
    pcardx=350
    pcardpos=1
    comcardx = 350
    comcardpos=1
    pygame.display.flip()
    shuffle(deck)
    ### set up player and dealer starting hand
    playerHand = []
    playerHand.append(deck[0])
    playerHand.append(deck[2])
    computerHand =[]
    computerHand.append(deck[1])
    computerHand.append(deck[3])

    ss = spritesheet.spritesheet('cards.jpg')
    # Sprite is 16x16 pixels at location 0,0 in the file...
    image = ss.image_at((playerHand[0].X, playerHand[0].Y, 50, 75))
    image2 = ss.image_at((playerHand[1].X, playerHand[1].Y, 50, 75))
    cardD1 = ss.image_at((20, 384, 50, 75))
    cardD2 = ss.image_at((computerHand[1].X, computerHand[1].Y, 50, 75))

    pygame.display.flip()
    cardsound.play()
    time.sleep(1)
    screen.blit(image2, (290, 250))

    pygame.display.flip()
    cardsound.play()
    time.sleep(1)
    screen.blit(cardD1, (290, 50))
    pygame.display.flip()
    cardsound.play()
    time.sleep(1)
    screen.blit(image, (350, 250))

    pygame.display.flip()
    cardsound.play()
    time.sleep(1)
    screen.blit(cardD2, (350, 50))
    pygame.display.flip()

    pygame.display.flip()
    print(computerHand[0].Hand)

### Begin Player's Turn
    cardcount = 4

    myturn = True
    while myturn == True:
        playerstrength = 0
        for card in playerHand:
            playerstrength += card.Number
        computerstrength=0
        for card in computerHand:
            computerstrength += card.Number
        if playerstrength==21:
            print("Player has 21!")
            myturn=False
        elif computerstrength==21:
            print("Sorry! Dealer has 21")
            myturn = False
        elif playerstrength>21:
            print("Player Busted")
            myturn=False
        elif playerstrength<21:
            print("Player has", str(playerstrength))



            playerhit=input("would you like to hit? y/n")
            if playerhit == ('y'):
                pcardx+=60
                pcardpos+=1
                playerHand.append(deck[cardcount])
                cardcount+=1
                image3 = ss.image_at((playerHand[pcardpos].X, playerHand[pcardpos].Y, 50, 75))
                cardsound.play()
                time.sleep(1)

                screen.blit(image3, (pcardx, 250))

                pygame.display.flip()
                print (playerHand[2].Hand)
                myturn=True
            if playerhit==('n'):
                myturn=False

### Begin Dealer's Turn
    cardD1 = ss.image_at((computerHand[0].X, computerHand[0].Y, 50, 75))
    screen.blit(cardD1, (290, 50))
    time.sleep(2)
    pygame.display.flip()
    dealerturn=True
    while dealerturn==True:
        dealerstrength=0
        for item in computerHand:
            dealerstrength=dealerstrength+item.Number
            print ("dealer Strength is", dealerstrength)
        if dealerstrength < 17:
            comcardx+=60
            comcardpos+=1
            computerHand.append(deck[cardcount])
            cardcount+=1
            cardD3 = ss.image_at((computerHand[comcardpos].X, computerHand[comcardpos].Y, 50, 75))
            cardsound.play()
            time.sleep(1)
            screen.blit(cardD3, (comcardx, 50))
            pygame.display.flip()
            dealerturn=True
        elif dealerstrength>=17 and dealerstrength <=21:
            print("Dealer has", dealerstrength)
            dealerturn=False
        elif dealerstrength>21:
            print("Dealer Busted!")
            dealerturn=False
    redeal=input("Deal again?")
    if redeal == ('y'):
        screen.fill((0, 51, 25))
        new_hand()
    else:
        global done
        done=True

new_hand()

done=False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
