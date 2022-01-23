
class Play:
    """Features of person who plays the game.

    The responsibility of Play is to keep track of score and to decide whether the 
    game should be continued.
   
    Attributes:
        score (int): current score of a player
        guess (str): higher or lower (h/l). Player's guess if the next card will worth
                     more or less than the current one. 
        cont_game: player's answer to a prompt to play
    """
    def __init__(self, score = 300, cont_game = "", guess = None):
        """Constructs a new Play.
        
        Args:
            self (Play): an instance of Play.
        """
        self.score = score
        self.guess = guess
        self.cont_game = cont_game