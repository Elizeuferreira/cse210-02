rom game.guess import Hilo

import random 

def show_card():
    card = random.randint(1,13)
    return card

def main():
    points = 300
    card = show_card()
    print("The card is: ", card)
    user = input("higher or lower (h/l): ")
    
    next_card = show_card()
    print("The next Card was: ", next_card)
    
    if card > next_card:
       if user == "l":
          points += 100 
       else:
          points -= 75
    else: 
        if user.upper == "h":
           points += 100
        else:
          points -= 75
    print("Your score is: ", points)
pass 
    
if __name__:"__main_"
main()

   
    
