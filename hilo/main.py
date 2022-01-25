from game import Dealer
from player import Play

def calculate_score(first_card, next_card, player):
    """Calculates current score.
        
        Args:
            first_card: previous card.
            next_card: card the player is guessing about.
            player: class of player 
    """
    h_l = "l" if next_card < first_card else "eq" if next_card == first_card  else "h"
    if h_l == "eq":
        None
    else:
        if player.guess == h_l:
            player.score += 100
        else:
            player.score -= 75
    return player 
    
def start_game(player, dealer):
    """The game itself. Starts and continues the game. 
        
        Args:
            player: object in which the value of a Play class have been passed.
            dealer: object in which the value of a Dealer class have been passed. 
    """
    while player.score > 0:
        first_card = dealer.show_card()
        print("The card is: ", first_card)
        player.guess = input("What is your guess: Higher or Lower: (h/l) ")
        while player.guess.lower() != "h" and player.guess.lower() != "l":
            print("Incorrect answer...")
            player.guess = input("What is your guess: Higher or Lower: (h/l) ")
        next_card = dealer.show_card()
        print("The card was: ", next_card)
        player = calculate_score(first_card, next_card, player)
        print("The score is: ", player.score)
        if player.score <= 0:
            break
        player.cont_game = input("Play again? (y/n) ")
        while player.cont_game.lower() != "y" and player.cont_game.lower() != "n":
            print("Incorrect answer...")
            player.cont_game = input("Play again? (y/n) ")
        if player.cont_game.lower() == "n":
            break
            
    print("========GAME OVER========")
dealer = Dealer()
player = Play() 

start_game(player, dealer)