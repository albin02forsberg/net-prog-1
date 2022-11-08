import random

from Card import Card


class CardDeck:
    def __init__(self, cards=[]):
        self._cards = cards
        for suit in range(1, 5):
            for value in range(1, 14):
                self._cards.append(Card(suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)

    def getCard(self):
        card = self._cards.pop()
        return card

    def size(self):
        return len(self._cards)

    def reset(self):
        self._cards = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self._cards.append(Card(suit, value))
