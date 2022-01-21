""" Documentation checker
A command-line tool for checking source code documentation requirements.
Authors:
  - Ogunniyi Owamamwen
"""
import random


def get_owamamwen_hilo():

    # The user can play again
    play_again = True
    low_score_table = [0, 100, 100, 100, 100]

    # loop the user can play again
    while play_again == True:
        winner = False
        guesses = 0

        print("\n=========== High Low Game ===========\n")
    # User input value
        print(""" Card range is 1 to 13 """)
        game_range = int(input("The Card is: "))

    #  Set the range of the input value
        if game_range == 1:
            game_size = 300
        elif game_range == 2:
            game_size = 310
        elif game_range == 3:
            game_size = 320
        elif game_range == 4:
            game_size = 330
        elif game_range == 5:
            game_size = 340
        elif game_range == 6:
            game_size = 350
        elif game_range == 7:
            game_size = 360
        elif game_range == 8:
            game_size = 370
        elif game_range == 9:
            game_size = 380
        elif game_range == 10:
            game_size = 390
        elif game_range == 11:
            game_size = 400
        elif game_range == 12:
            game_size = 410
        elif game_range == 13:
            game_size = 3420

        game_number = random.randint(1, game_size)
        print("You score is: " + str(game_number))

        # Know the low score
        print("\nThe current low score for this level is: " +
              str(low_score_table[game_range]) + " guesses.\n")

        user_guess = int(input("Enter your guess: "))

        # Help the player
        hint_question = str(
            input("\nWould you like a hint for 2 guesses y/n? "))
        hint_question = hint_question.lower()

    # Check if the number is even or odd
        if hint_question == "y":
            guesses = guesses + 2
        if game_number % 2 == 0:
            print("The Number is EVEN")
        else:
            print("The Number is ODD")

        if user_guess == game_number:
            print("--=== You Win ===--\n")
            winner = True
            if low_score_table[game_range] > guesses:
                low_score_table[game_range] == guesses
        elif user_guess > game_number:
            print("Too High\n")
        else:
            print("Too Low\n")

        print("End of game. You solved this in " + str(guesses) + " guesses.")

    # Asking the user if he/she want to play again
        another_game = str(input("would you like to play again y/n? "))
        another_game = another_game.lower()
        if another_game == "y":
            play_again = True
        else:
            play_again = False

    print("\n------ Thank you for playing ------\n")