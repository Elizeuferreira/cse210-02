import random
starting_points=300
terminate=False
usable_cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
cards_used=[]
print("Lets begin!")
card_drawn=random.choice(usable_cards)
index=usable_cards.index(card_drawn)
usable_cards.pop(index)
cards_used.append(index+1)
#print("List of Usable Cards")
#print(usable_cards)
#print("List of cards used...")
#print(cards_used)


print(f"The first card is a {card_drawn}")
previous_card=int(card_drawn)
#print(f"previous_card={card_drawn}")

def draw_card():
    print("Drawing a new card...")
    if usable_cards==False:
        print("There are no more cards to be drawn.")
        return
    else:
        pass
    card_drawn=random.choice(usable_cards)
    index=usable_cards.index(card_drawn)
    usable_cards.pop(index)
    cards_used.append(index+1)
    print(f"The card I drew was a {card_drawn}.")
    return card_drawn


while starting_points > 0 or terminate!=True:
    draw_card()
    user_guess=input("Is the card I am holding higher or lower? ")