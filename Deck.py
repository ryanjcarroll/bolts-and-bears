import json
import os
import pandas as pd

class Deck():
    def __init__(self, decklist_path='sample_decklist.txt', cardlist_path='cardlist.txt'):
        
        # import full card pool
        with open(cardlist_path) as cardlist_in:
            cardlist = json.load(cardlist_in)

        # import decklist
        with open(decklist_path) as decklist_in:
            decklist = decklist_in.read()

        deck_as_list = []
        # for each line in decklist, add that card N times
        for line in decklist.split('\n'):
            qty = int(line.split(' ')[0])
            cardname = ' '.join(line.split(' ')[1:])

            # get the attributes of each card from the cardlist
            card_info = list(filter(lambda card: card['name'] == cardname, cardlist))
            for q in range(qty):
                deck_as_list.append(card_info)

        # create deck as a dataframe
        self.df = pd.DataFrame(deck_as_list)

    # randomize the card order
    def shuffle(self):
        self.df = self.df.sample(frac=1).reset_index(drop=True)

    # return the top card of the deck, then remove it from the deck
    def draw(self):
        drawn_card = self.df.iloc[0].values.tolist()[0]
        self.df = self.df.iloc[1:]

        return drawn_card