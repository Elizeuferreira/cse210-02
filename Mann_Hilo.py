from ast import While
import random
points=300
terminate=False
usable_cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
cards_used=[]

def main():
    print("Lets begin!")
    print(f"Starting Score:{points}")
    card_drawn=random.choice(usable_cards)
    index=usable_cards.index(card_drawn)
    usable_cards.pop(index)
    cards_used.append(index+1)
    #print("List of Usable Cards")
    #print(usable_cards)
    #print("List of cards used...")
    #print(cards_used)
    print(f"The first card is {card_drawn}")
    user_guess=input("Is the next card going to be higher or lower? Type N to stop. ").lower()
    previous_card=int(card_drawn)
    draw_card(previous_card, user_guess, points)


def draw_card(previous_card, user_guess,points):
    while points > 0:
        if usable_cards==False:
            print("There are no more cards to be drawn.")
            print(f"Score:{points}")
            quit()
        else:
            card_drawn=random.choice(usable_cards)
            index=usable_cards.index(card_drawn)
            usable_cards.pop(index)
            cards_used.append(index+1)

        if user_guess=="h":
            print("Drawing a new card...")
            if previous_card < card_drawn:
                print("Correct!")
                points=points+100
                print(f"Score:{points}")
                previous_card=card_drawn
            else:
                print("Incorrect...")
                points=points-75
                print(f"Score:{points}")
                previous_card=card_drawn

        elif user_guess=="l":
            print("Drawing a new card...")

            if previous_card > card_drawn:
                print("Correct!")
                points=points+100
                print(f"Score:{points}")
                previous_card=card_drawn
            else:
                print("Incorrect...")
                points=points-75
                print(f"Score:{points}")
                previous_card=card_drawn
        elif user_guess=="n":
            print("Thanks for playing.")
            print(f"Score:{points}")
            quit()
        else:
            print("Invalid input.  Penalty Applied.")
            points=points-75
            print(f"Score:{points}")
            
        #print(f"The card I drew was a {card_drawn}.")
        return

main()
