# rock_paper_scissors

### Introduction

Basically, this program describes a ROCK PAPER SCISSOR game between two players (Human and Computer), where each player is allowed to make a choice as either R (Rock), P(Paper) or S(Scissor).

### Game Rule

1. A user or Computer is allowed to make either of the three choices (R, P or S). when an anvalid choice is entered, the user is prompted to enter a valid choice of character that conforms to the characters of the game.
   However, for the Computer, the system randomly selects a choice. To achieve this, I made use of [using choice in python.](https://pynative.com/python-random-choice/#h-python-random-choice-function)

2. The game is expected to terminate if and only if a winner emerges. Hence, if there's a draw, the user and computer keeps playing.
   we assume the commputer is also allowed to think for 2 to 4 seconds before making a move. Just to make it fun, to achieve this I used [time function](https://www.tutorialspoint.com/python/time_sleep.htm).

### Rules to declare a winner

A winner is declared if the following pairs is entered by the Player(Human) or Computer. Depending on the choices entered by both players, a win is determine if;

1. if one player enters ROCK and the other player enters SCISSOR. Hence, ROCK beats SCISSOR
2. if one player enters PAPER and the other player enters ROCK. Hence, PAPER beats ROCK
3. if one player enters SCISSOR and the other player enters PAPER. Hence, SCISSOR beats PAPER

Here is a link to find out more about the game and it's rule [rock_paper_scissor game and rules](https://www.playworks.org/game-library/ro-sham-bo-or-rock-paper-scissors/)
