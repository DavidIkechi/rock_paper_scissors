import random as rd
import time



def game_rules():
    """In this function, we just print out the rules of the game.
    """
    print("IMPLEMENTING THE ROCK PAPER SCISSORS GAME")
    print("Participants: PLAYER VS COMPUTER")
    print("{}".format("-"*40))
    print("GAMES RULES NOTE: THERE MUST BE A WINNER")
    print("To win \nRock beats Scissors\nPaper beats Rock \nScissors beats Paper ")    
    print("Same character indicates draw")
    print("{}".format("-"*40))
    print("\nBEGIN")
    print("{}".format("-"*40))

    

def comp_choice(item_list):
    """ This function randomly select an item from a list

    Args:
        item_list (list): a list of string, which contains choice for the game
    
    Returns:
        A string which represent the randomly selected item in the list
    """
    # get the selected item
    selected_item = rd.choice(item_list) 
    return selected_item
    

def get_user_input(valid_characters):
    """This function accepts input from a user, ensuring the input matches with valid characters

    Args:
        valid_characters (list): represents a valid list of items that verifies a user's input

    Returns:
        string: A value which represents the user's input
    """
    print("please enter R for Rocks\nP for Paper\nS for Scissors\n")
    # get the user input and convert it to an uppercase
    # to compare adequately with what we have in our list
    get_input = input("Enter selection: ").upper().strip()
    
    while get_input not in valid_characters:
        print("You have entered an invalid selection\n")
        print("please enter R for Rocks\nP for Paper\nS for Scissors\n")

        get_input = input("Enter selection: ").upper().strip()
  
    return get_input
    
    
def play_game(player1, computer):
    """This function initiates the Rock, paper, Scissors game

    Args:
        player1 (string): represents the players input or choice
        computer (string): represents computer choice

    Returns:
        string: A value which represents the game decision as win for player or computer, or draw.
    """
    
    check_board = {"R":"ROCK", "P":"PAPER", "S":"SCISSORS"}
    print("player move: {:<12} \nComputer move {:<12}\n\n".format(check_board[player1],
                                                                check_board[computer]))
    
    # note we have three winning category
    winner_board = [["R","S"], ["P","R"],["S","P"]]
    
    # we assume you win if [player1, computer] list input matches our winner_board
    # In a case where player1 and computer have same 
    if player1 == computer:
        return "draw"
    elif [player1,computer] in winner_board:
        return "you win\n{} beats {}".format(check_board[player1], check_board[computer])
    else:
        return "Computer wins\n{} beats {}".format(check_board[computer], check_board[player1])


########################################################################################################
# define a list to store the characters for the game
characters = ["R","P","S"]
# start the game
start_game = True
while start_game:
    # start the game, first output the game rules
    game_rules()
    
    # get the user input
    player1_input = get_user_input(characters)
    # get the computer choice
    print("\nComputer's turn")
    print("To make it fun, we assume computer is thinking too")
    # we want the computer to think small.
    thinking = rd.randint(2, 4)
    print("thinking... for {} secs".format(thinking))
    time.sleep(thinking)
    computer_input = comp_choice(characters)
    
    # play the game
    get_score = play_game(player1_input, computer_input)
    
    # Iif there is a draw, keep on playing. 
    while get_score.lower() == "draw":
        print("Opps that's a draw, we need a winner \nyou have to keep playing\n")
        player1_input = get_user_input(characters)
        print("\nComputer's turn")
        thinking = rd.randint(2, 4)
        print("thinking... for {} secs".format(thinking))
        time.sleep(thinking)
        computer_input = comp_choice(characters)
        get_score = play_game(player1_input, computer_input)
        
    # End Game
    start_game = False
    
print("{}".format("-"*40))
print(get_score.upper())
print("Good bye o!")
        
    
