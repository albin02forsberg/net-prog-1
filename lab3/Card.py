class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
        # if(self._value == 1):
        #     return "Ace"
        # elif(self._value == 11):
        #     return "Jack"
        # elif(self._value == 12):
        #     return "Queen"
        # elif(self._value == 13):
        #     return "King"
        # else:
        #     return self._value
        return self._value

    def getSuit(self):
        # if(self._suit == 1):
        #     return "Spades"
        # elif(self._suit == 2):
        #     return "Hearts"
        # elif(self._suit == 3):
        #     return "Clubs"
        # elif(self._suit == 4):
        #     return "Diamonds"
        return self._suit

    def __str__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

        if(self._value == 1):
            return "Ace of " + suits[self._suit - 1]
        elif(self._value == 11):
            return "Jack of " + suits[self._suit - 1]
        elif(self._value == 12):
            return "Queen of " + suits[self._suit - 1]
        elif(self._value == 13):
            return "King of " + suits[self._suit - 1]
        else:
            return str(self._value) + " of " + suits[self._suit - 1]
