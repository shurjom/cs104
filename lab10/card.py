# Lab 10, CS104 Card Game: War
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <11.12.15>

#initialization 
from __future__ import division, print_function
input = raw_input 

import random

# constant definitions here

# function definitions here 
def newCard(number, suit):
    card = (number, suit)
    return card

def cardToString():
    cardString = ""
    if card[0] < 11:
        cardString += str(card[0])
    elif card[0] == 11:
        cardString += "Jack"
    elif card[0] == 12:
        cardString += "Queen"
    elif card[0] == 13:
        cardString += "King"
    elif card[0] == 14:
        cardString += "Ace"
    
    cardString += " of "
    if card[1] == "H":
        cardString += "Hearts"
    elif card[1] == "D":
        cardString += "Diamonds"
    elif card[1] == "S":
        cardString += "Spades"
    elif card[1] == "C":
        cardString += "Clubs"
        
def newDeck():
    deck = []
    for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
        for i in range(2,15):
            deck.append(newCard(i, suit))
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def compare(card1, card2):
    if card1 < card2:
        return -1
    if card1 == card2:
        return 0
    else:
        return 1

# --------- main program -------------

if __name__ == "__main__":   
    card = newCard(3, "D")
    assert card == (3, 'D')   