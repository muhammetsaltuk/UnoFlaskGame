import random


def buildDeck(): # deste oluşturma kodu
    deck = []
    colours = ["red", "green", "yellow", "blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "drawtwo", "skip", "reverse"]
    wilds = ["wild", "wilddrawfour"]
    for colour in colours:
        for value in values:
            cardVal = "{}-{}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    random.shuffle(deck)
    return deck
