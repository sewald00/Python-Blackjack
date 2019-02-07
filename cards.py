from random import shuffle
import spritesheet
import pygame

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Python Black Jack")
screen.fill((0, 51, 25))

#(x,y) position is for sprite sheet location of each card
class card:
    def __init__(self,hand,suit,number,text,x,y):
        self.Hand=hand
        self.Suit=suit
        self.Number=number
        self.Text=text
        self.X=x
        self.Y=y


#create hearts
aceH=card('Ah','hearts',11,'Ace of Hearts',75,383)
kingH=card('Kh','hearts',10,'King of Hearts',130,384)
queenH=card('Qh','hearts',10,'Queen of Hearts',183,383)
jackH=card('Jh','hearts',10,'Jack of Hearts',236,383)
tenH=card('10h','hearts',10,'Ten of Hearts',290,383)
nineH=card('9h','hearts',9,'Nine of Hearts',344,383)
eightH=card('8h','hearts',8,'Eight of Hearts',399,383)
sevenH=card('7h','hearts',7,'Seven of Hearts',452,383)
sixH=card('6h','hearts',6,'Six of Hearts',505,383)
fiveH=card('5h','hearts',5,'Five of Hearts',559,383)
fourH=card('4h','hearts',4,'Four of Hearts',613,383)
threeH=card('3h','hearts',3,'Three of Hearts',666,383)
twoH=card('2h','hearts',2,'Two of Hearts',720,383)
#create diamonds
aceD=card('Ad','diamonds',11,'Ace of Diamonds',75,225)
kingD=card('Kd','diamonds',10,'King of Diamonds',129,225)
queenD=card('Qd','diamonds',10,'Queen of Diamonds',183,225)
jackD=card('Jd','diamonds',10,'Jack of Diamonds',236,225)
tenD=card('10d','diamonds',10,'Ten of Diamonds',290,225)
nineD=card('9d','diamonds',9,'Nine of Diamonds',344,225)
eightD=card('8d','diamonds',8,'Eight of Diamonds',397,225)
sevenD=card('7d','diamonds',7,'Seven of Diamonds',451,225)
sixD=card('6d','diamonds',6,'Six of Diamonds',504,225)
fiveD=card('5d','diamonds',5,'Five of Diamonds',558,225)
fourD=card('4d','diamonds',4,'Four of Diamonds',613,225)
threeD=card('3d','diamonds',3,'Three of Diamonds',666,225)
twoD=card('2d','diamonds',2,'Two of Diamonds',720,225)

#create spades
aceS=card('As','spades',11,'Ace of Spades',75,302)
kingS=card('Ks','spades',10,'King of Spades',129,302)
queenS=card('Qs','spades',10,'Queen of Spades',183,302)
jackS=card('Js','spades',10,'Jack of Spades',236,302)
tenS=card('10s','spades',10,'Ten of Spades',290,302)
nineS=card('9s','spades',9,'Nine of Spades',344,302)
eightS=card('8s','spades',8,'Eight of Spades',397,302)
sevenS=card('7s','spades',7,'Seven of Spades',451,302)
sixS=card('6s','spades',6,'Six of Spades',504,302)
fiveS=card('5s','spades',5,'Five of Spades',558,302)
fourS=card('4s','spades',4,'Four of Spades',613,302)
threeS=card('3s','spades',3,'Three of Spades',666,302)
twoS=card('2s','spades',2,'Two of Spades',720,302)

#create clubs
aceC=card('Ac','clubs',11,'Ace of Clubs',75,145)
kingC=card('Kc','clubs',10,'King of Clubs',129,145)
queenC=card('Qc','clubs',10,'Queen of Clubs',183,145)
jackC=card('Jc','clubs',10,'Jack of Clubs',236,145)
tenC=card('10c','clubs',10,'Ten of Clubs',290,145)
nineC=card('9c','clubs',9,'Nine of Clubs',344,145)
eightC=card('8c','clubs',8,'Eight of Clubs',397,145)
sevenC=card('7c','clubs',7,'Seven of Clubs',451,145)
sixC=card('6c','clubs',6,'Six of Clubs',504,145)
fiveC=card('5c','clubs',5,'Five of Clubs',558,145)
fourC=card('4c','clubs',4,'Four of Clubs',613,145)
threeC=card('3c','clubs',3,'Three of Clubs',666,145)
twoC=card('2c','clubs',2,'Two of Clubs',720,145)

#create full deck
deck=[aceH,kingH,queenH,jackH,tenH,nineH,eightH,sevenH,sixH,fiveH,fourH,threeH,twoH,
      aceD,kingD,queenD,jackD,tenD,nineD,eightD,sevenD,sixD,fiveD,fourD,threeD,twoD,
      aceS,kingS,queenS,jackS,tenS,nineS,eightS,sevenS,sixS,fiveS,fourS,threeS,twoS,
      aceC,kingC,queenC,jackC,tenC,nineC,eightC,sevenC,sixC,fiveC,fourC,threeC,twoC]


def new_hand():
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


    screen.blit(image, (350, 250))
    screen.blit(image2, (290, 250))
    screen.blit(cardD1, (290, 50))
    screen.blit(cardD2, (350, 50))
    pygame.display.flip()
    print(computerHand[0].Hand)

    cardcount=4

    playerhit=input("would you like to hit? y/n")
    if playerhit == ('y'):
        playerHand.append(deck[cardcount])
        cardcount+=1
        image3 = ss.image_at((playerHand[2].X, playerHand[2].Y, 50, 75))
        screen.blit(image3, (410, 250))
        pygame.display.flip()
        print (playerHand[2].Hand)
    if playerhit==('n'):
        cardD1 = ss.image_at((computerHand[0].X, computerHand[0].Y, 50, 75))
        screen.blit(cardD1, (290, 50))
        pygame.display.flip()
        dealerstrength=0
        for item in computerHand:
            dealerstrength=dealerstrength+item.Number
        print ("dealer Strength is", dealerstrength)
        if dealerstrength < 17:
            computerHand.append(deck[cardcount])
            cardD3 = ss.image_at((computerHand[2].X, computerHand[2].Y, 50, 75))
            screen.blit(cardD3, (410, 50))
            pygame.display.flip()
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
