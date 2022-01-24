Overview
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Rules
Hilo is played according to the following rules:
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

Project structure:
The project consists of 3 .py files: game, player and main.
In "game" file class of Dealer is created with it's attribute "card"
which randomly picks a card with value varying from 1 to 13.
In "play" file Player class is created. Its attributes "score", "guess" 
and "cont_game" are responsible to track currcnt score, choose higher 
or lower card will be and determines whether or not the game be continued
respectively. 
The "main" file imports Play and Dealer classes and uses "calculate_score" 
and "start_game" methods to run the game. 

Required software: VS-code (or other program to run the code), Python 3.

Team members:            
Brenner Mann,
Elizeu Ferreira,
Josifini Tamanalevu,
Mahonrri Mendez,
Shawn Yang,
Alexander Karasik (kar21020@byui.edu).
