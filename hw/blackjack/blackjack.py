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

def is_win(hand, dhand):
    return (sum([x.value for x in hand]) <= 21 and sum([x.value for x in hand]) > sum([x.value for x in dhand]))
def main():
    pile = Deck()
    pile.shuffle()
    hand = []
    hand += [pile.deal(), pile.deal()]
    dhand = []
    dhand += [pile.deal(), pile.deal()]
    if (sum([x.value for x in hand]) == 21):
        print("You win!")
    print("Hand: " + str(hand))
    ans = input("Would you like a card? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Enter y for yes and n for no: ")
    if ans == 'y':
        hand += [pile.deal()]
    if (sum([x.value for x in dhand]) < 18):
        dhand += [pile.deal()]
    print("Hand: " + str(hand))
    while (sum([x.value for x in hand]) < 21 and ans != 'n'):
        ans = input("Would you like a card? (y/n): ")
        while (ans != 'y' and ans != 'n'):
            ans = input("Enter y for yes and n for no: ")
        if ans == 'y':
            hand += [pile.deal()]
        print("Hand: " + str(hand))
        if (sum([x.value for x in dhand]) < 18):
            dhand += [pile.deal()]
    if (is_win(hand,dhand)):
        print("You win!")
        print("Your hand:", hand)
        print("Dealer's hand:", dhand)
    else:
        print("You lose!")
        print("Your hand:", hand)
        print("Dealer's hand:", dhand)

if __name__ == '__main__':
    main()
