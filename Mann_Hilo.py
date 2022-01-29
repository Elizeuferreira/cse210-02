#Brenner Mann

# Library Imports
import random

#Starting Points
points=300

#Starting Lists
usable_cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
cards_used=[]

#Main Definition
def main():
   startup()

#Code that will start the program.  
def startup():
    print("Lets begin!")
    print(f"Starting Score:{points}")

    #This block of code will choose 
    # and remove a random 'card' from the list.  
    #It will then add the 'card' to the second, unusable list.

    card_drawn=random.choice(usable_cards)
    index=usable_cards.index(card_drawn)
    usable_cards.pop(index)
    cards_used.append(index+1)
    print(f"The first card is {card_drawn}")

    # First User Prompt.
    user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()
    previous_card=int(card_drawn)
    draw_card(previous_card, user_guess, points)

#While loop using the first user prompt.  
#loop will stop whenever the user inputs "n"
#Will penalize a player if they do not use the three accepted inputs.
def draw_card(previous_card, user_guess,points):
    while points > 0:
        # Code that will stop the loop if the card list is empty.
        if len(usable_cards)==0:
            print("____________________________________________________")
            print("There are no more cards to be drawn.")
            print(f"Score:{points}")
            print()
            quit()
        else:
            card_drawn=random.choice(usable_cards)
            index=usable_cards.index(card_drawn)
            usable_cards.pop(index)
            cards_used.append(index+1)
        #Code for when the user types in "h"
        #Will subtract points if the user is incorrect.
        if user_guess=="h":
            print("Drawing a new card...")
            if previous_card < card_drawn:
                print("Correct!")
                print(f"The card I drew was a {card_drawn}!")
                points=points+100
                print(f"Score:{points}")
                previous_card=card_drawn
                user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()
                print()
            else:
                print("Incorrect...")
                print(f"The card I drew was a {card_drawn}.")
                points=points-75
                print(f"Score:{points}")
                previous_card=card_drawn
                user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()
                print()

        #Code for when the user types in "l"
        #Will subtract points if the user is incorrect.
        elif user_guess=="l":
            print("Drawing a new card...")
            if previous_card > card_drawn:
                print("Correct!")
                points=points+100
                print(f"The card I drew was a {card_drawn}!")
                print(f"Score:{points}")
                previous_card=card_drawn
                user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()
                print()

            else:
                print("Incorrect...")
                points=points-75
                print(f"The card I drew was a {card_drawn}.")
                print(f"Score:{points}")
                previous_card=card_drawn
                user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()
                print()
        #Code for when the user types in "n"
        #Immediatly terminates the program.
        elif user_guess=="n":
            print("Thanks for playing.")
            print(f"Score:{points}")
            quit()

        #Code for when the user types in any incorrect input.
        #Penalizes player and allows the player to continue.
        else:
            print("Invalid input.  Penalty Applied.")
            points=points-75
            print(f"Score:{points}")
            print()
            user_guess=input("Is the next card going to be higher or lower? Type n to stop. ").lower()

        #Code that stops the loop if the player's points become negative.
        #Note: Game will continue to play if the player has 0 points.
        #Runs as a last chance senario. 
    if points < 1:
        print("You ran out of points.")
        print("Game Over.")
        quit()

main()
