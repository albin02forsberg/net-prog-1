class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
        if(self._value == 1):
            return "Ace"
        elif(self._value == 11):
            return "Jack"
        elif(self._value == 12):
            return "Queen"
        elif(self._value == 13):
            return "King"
        else:
            return self._value

    def getSuit(self):
        if(self._suit == 1):
            return "Spades"
        elif(self._suit == 2):
            return "Hearts"
        elif(self._suit == 3):
            return "Clubs"
        elif(self._suit == 4):
            return "Diamonds"

    def __str__(self):
        return str(self.getValue()) + " of " + str(self.getSuit())
