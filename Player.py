from Deck import *

class Player():
    def __init__(self, life_total=20, decklist_path='sample_decklist.txt'):
        self.life_total = life_total

        self.deck = Deck(decklist_path=decklist_path)
        self.deck.shuffle()

        self.hand = []
        for i in range(7):
            self.draw()

        self.lands_in_play = 0
        self.mana_available = 0

    def draw(self):
        self.hand.append(self.deck.draw())

    def remove(self, card):
        self.hand.remove(card)

    def add_land(self):
        self.lands_in_play += 1
        self.mana_available += 1