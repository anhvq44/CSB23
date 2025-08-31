import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return f'{self.value} of {self.suit}'
    
class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['heart', 'diamond', 'club', 'spade']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
                
    def __str__(self):
        return f'Deck of {len(self.cards)} cards: {', '.join(str(card) for card in self.cards)}'
    
    def shuffle(self):
        if not self.cards:
            return 'The deck is empty.'
        return random.shuffle(self.cards)
    
    def deal_a_card(self):
        if not self.cards:
            return 'The deck is empty.'
        self.cards.pop(0)
        
    def sort(self):
        value_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4,
                       '7': 5, '8': 6, '9': 7, '10': 8,
                       'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        suit_order = {'heart': 0, 'diamond': 1, 'club': 2, 'spade': 3}
        self.cards.sort(key=lambda card: (suit_order[card.suit], value_order[card.value]))
    
    
deck = Deck()
print("INITIALIZE DECK:", deck, "\n")

deck.shuffle()
print("DECK AFTER SHUFFLE:", deck, "\n")
deck.deal_a_card()

print("DECK AFTER DEAL:", deck, "\n")
deck.deal_a_card()

print("DECK AFTER DEAL:", deck, "\n")
deck.sort()

print("DECK AFTER SORT:", deck, "\n")
