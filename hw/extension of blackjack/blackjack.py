import random

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]
    def __repr__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]

class Deck:
    def __init__(self):
        self.cards = [Card(i,j) for i in range(1,14) for j in range(0,4)]
    
    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        top = self.cards[0]
        self.cards.pop(0)
        return top

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 0
    
    def get_sum(self):
        return sum([card.value for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

class Game:
    def __init__(self, player):
        self.deck = Deck()
        self.player = player
        self.player.cards = []
        self.player.money = int(self.player.money)
        self.player.money -= 100
        self.deck.shuffle()
        print(' Welcome to the game! ')


    def turn(self):
        card = self.deck.deal()
        self.player.add_card(card)

        print('You cards: ' + str(self.player.cards))

        if (self.player.get_sum() > 21):
            return False
        elif (self.player.get_sum() <= 21):
            return True
        
    
    def stop(self):
        s = self.player.get_sum()
        payoff = 0
        if (s>21):
            payoff = -200
        if (s==21):
            payoff = 500
        elif (s==20):
            payoff = 300
        elif (s==19):
            payoff = 200
        elif (s==18):
            payoff = 150
        elif (s==17):
            payoff = 50
        elif (s==16):
            payoff = 10
        elif (s==15):
            payoff = -10
        elif (s==14):
            payoff = -50
        elif (s==13):
            payoff = -100

        
        self.player.money += payoff
        
        return payoff


