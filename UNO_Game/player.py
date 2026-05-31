class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self,deck):
        card = deck.draw()
        self.hand.append(card)

    def play_card(self,index):
        return self.hand.pop(index)

    def has_won(self):
        return len(self.hand) == 0