import random
   
class Dealer:
    def __init__(self, card=None):
        self.card = card
    def show_card(self):
        self.card = random.randint(1,13)
        return self.card
        

           
    