from CardDeck import CardDeck


deck = CardDeck()
deck.shuffle()
while deck.size() > 0:
    card = deck.getCard()
    print(card)
