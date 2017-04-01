from card import *

deck = newDeck()
shuffleDeck(deck)

player1 = []
player2 = []
for idx in range(0,len(deck),2):
    player1.append(deck[idx])
    player2.append(deck[idx + 1])

while player1 != [] and player2 != []:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    compare(card1,card2)
    if card1==1:
        player1.append(card2)
    elif card1==-1:
        player2.append(card1)
    elif card1==0:
        win = random.randint(0,1)
        if win == 1:
            player1.append(card2)
        else:
            player2.append(card1)
    print (player1)
    print (player2)
if len(player1)>len(player2):
    print ("Player 1 won!")
else:
    print ("Player 2 won!")