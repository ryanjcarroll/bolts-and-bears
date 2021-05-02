from Player import *

class Game():
    def __init__(self):
        self.game_over = False
        self.p1 = Player()
        self.p2 = Player()
        self.players = [self.p1, self.p2]

        self.turn = 0
    def initialize(self):
        self.p1.deck.shuffle()

    def run(self):
        while not self.game_over:
            self.turn += 1
            print('---TURN {}---'.format(self.turn))

            played_land = False

            # untap lands
            self.p1.mana_available = self.p1.lands_in_play

            # draw card for turn
            self.p1.draw()
            print('Player 1 draws a card.')
            
            # play land for turn
            for card in self.p1.hand:
                if played_land:
                    break
                elif card['type'] == 'Basic Land':
                    self.p1.remove(card)
                    self.p1.add_land()
                    played_land = True
                    print('Player 1 plays a {}.'.format(card['name']))
                    print(self.p1.mana_available)

            # play spells
            while self.p1.mana_available > 0:
                for card in self.p1.hand:
                    if card['type'] in ['Creature','Instant']:
                        if card['mana_value'] <= self.p1.mana_available:
                            self.p1.remove(card)
                            self.p1.mana_available -= card['mana_value']
                            print('Player 1 plays a {}.'.format(card['name']))
                            self.p2.life_total -= 3
                            print('Player 2 life total drops to {}.'.format(self.p2.life_total))
        
            for player in self.players:
                if player.life_total <= 0:
                    self.game_over = True
                    print('Game Over')
                    break


g = Game()
g.run()