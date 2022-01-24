# import random
   
# class Dealer:
#     def __init__(self, card=None):
#         self.card = card
#     def show_card(self):
#         self.card = random.randint(1,13)
#         return self.card
#testando
import random
   
class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.
    Attributes:
        card: A value of randomly chosen card (from 1 to 13).
    """
    def __init__(self, card=None):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.card = card

    def show_card(self):
        """Randomly chooses and returns value of card.
        Args:
            self (Dealer): An instance of Dealer.
        """
        self.card = random.randint(1,13)
        return self.card       
    