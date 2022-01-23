from game import Dealer
from player import Play

def calculate_score(first_card, next_card, player):
    
    h_l = "l" if next_card < first_card else "h"
    if player.guess == h_l:
        player.score += 100
    else:
        player.score -= 75
        
    return player 
    
def start_game(player, dealer):
    while player.score > 0:
        first_card = dealer.show_card()
        print("The card is: ", first_card)
        player.guess = input("What is your guess: Higher or Lower: (h/l) ")
        next_card = dealer.show_card()
        print("The card was: ", next_card)
        player = calculate_score(first_card, next_card, player)
        print("The score is: ", player.score)
        player.cont_game = input("Play again? (y/n) ")
        if player.cont_game.lower() == "n":
            break
            
    print("========GAME OVER========")
dealer = Dealer()
player = Play() 

start_game(player, dealer)