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
kingD=card('Kd','hearts',10,'King of Diamonds',129,225)
queenD=card('Qd','hearts',10,'Queen of Diamonds',183,225)
jackD=card('Jd','hearts',10,'Jack of Diamonds',236,225)
tenD=card('10d','hearts',10,'Ten of Diamonds',290,225)
nineD=card('9d','hearts',9,'Nine of Diamonds',344,225)
eightD=card('8d','hearts',8,'Eight of Diamonds',397,225)
sevenD=card('7d','hearts',7,'Seven of Diamonds',451,225)
sixD=card('6d','hearts',6,'Six of Diamonds',504,225)
fiveD=card('5d','hearts',5,'Five of Diamonds',558,225)
fourD=card('4d','hearts',4,'Four of Diamonds',613,225)
threeD=card('3d','hearts',3,'Three of Diamonds',666,225)
twoD=card('2d','hearts',2,'Two of Diamonds',720,225)

#create spades
aceS=card('As','diamonds',11,'Ace of Diamonds',75,302)
kingS=card('Ks','hearts',10,'King of Diamonds',129,302)
queenS=card('Qs','hearts',10,'Queen of Diamonds',183,302)
jackS=card('Js','hearts',10,'Jack of Diamonds',236,302)
tenS=card('10s','hearts',10,'Ten of Diamonds',290,302)
nineS=card('9s','hearts',9,'Nine of Diamonds',344,302)
eightS=card('8s','hearts',8,'Eight of Diamonds',397,302)
sevenS=card('7s','hearts',7,'Seven of Diamonds',451,302)
sixS=card('6s','hearts',6,'Six of Diamonds',504,302)
fiveS=card('5s','hearts',5,'Five of Diamonds',558,302)
fourS=card('4s','hearts',4,'Four of Diamonds',613,302)
threeS=card('3s','hearts',3,'Three of Diamonds',666,302)
twoS=card('2s','hearts',2,'Two of Diamonds',720,302)

#create clubs
aceC=card('Ac','diamonds',11,'Ace of Diamonds',75,145)
kingC=card('Kc','hearts',10,'King of Diamonds',129,145)
queenC=card('Qc','hearts',10,'Queen of Diamonds',183,145)
jackC=card('Jc','hearts',10,'Jack of Diamonds',236,145)
tenC=card('10c','hearts',10,'Ten of Diamonds',290,145)
nineC=card('9c','hearts',9,'Nine of Diamonds',344,145)
eightC=card('8c','hearts',8,'Eight of Diamonds',397,145)
sevenC=card('7c','hearts',7,'Seven of Diamonds',451,145)
sixC=card('6c','hearts',6,'Six of Diamonds',504,145)
fiveC=card('5c','hearts',5,'Five of Diamonds',558,145)
fourC=card('4c','hearts',4,'Four of Diamonds',613,145)
threeC=card('3c','hearts',3,'Three of Diamonds',666,145)
twoC=card('2c','hearts',2,'Two of Diamonds',720,145)

#create full deck
deck=[aceH,kingH,queenH,jackH,tenH,nineH,eightH,sevenH,sixH,fiveH,fourH,threeH,twoH,
      aceD,kingD,queenD,jackD,tenD,nineD,eightD,sevenD,sixD,fiveD,fourD,threeD,twoD,
      aceS,kingS,queenS,jackS,tenS,nineS,eightS,sevenS,sixS,fiveS,fourS,threeS,twoS,
      aceC,kingC,queenC,jackC,tenC,nineC,eightC,sevenC,sixC,fiveC,fourC,threeC,twoC]


