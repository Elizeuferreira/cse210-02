import random 

def show_card():
    card = random.randint(1,13)
    return card

def main():
    points = 300
    card = show_card()
    print("The card is: ", card)
    user = input("higher or lower (h/l): ")
    print(user)
    
    next_card = show_card()
    print("The next Card was: ", next_card)
    
    if card > next_card:
       if user == "l":
          points += 100 
       else:
          points -= 75
    else: 
        if user == "h":
           points += 100
        else:
          points -= 75
    print("You score is: ", points)

class hilo_game(start, round):

    

    

    





